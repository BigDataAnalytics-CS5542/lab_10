import re
import numpy as np
from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer, util
from src.schemas import ProcessedReview, DetectionResult
from src.dictionaries import SUBSTANCE_TERMS, DISTRESS_AND_RELAPSE_TERMS

class RuleDetector:
    """Fast regex-based matching for high-precision baseline detection."""
    def __init__(self):
        # Compile all regex patterns on initialization for maximum speed
        self.substance_patterns = {
            category: re.compile("|".join(patterns), re.IGNORECASE)
            for category, patterns in SUBSTANCE_TERMS.items()
        }
        self.distress_pattern = re.compile(
            "|".join(DISTRESS_AND_RELAPSE_TERMS), re.IGNORECASE
        )

    def detect(self, text: str) -> Tuple[List[str], bool]:
        """
        Input: Cleaned review string
        Output: Tuple of (Detected substance categories, Boolean distress flag)
        """
        detected_substances = []
        for category, pattern in self.substance_patterns.items():
            if pattern.search(text):
                detected_substances.append(category)
                
        has_distress = bool(self.distress_pattern.search(text))
        
        return detected_substances, has_distress


class EmbeddingDetector:
    """Lightweight semantic similarity for catching nuanced/veiled distress."""
    def __init__(self):
        from dotenv import load_dotenv
        import os

        load_dotenv()

        HF_TOKEN = os.getenv("HF_TOKEN")

        # all-MiniLM-L6-v2 is extremely fast, runs locally, and takes <100MB of RAM
        self.model = SentenceTransformer('all-MiniLM-L6-v2',token=HF_TOKEN)
        
        # 'Anchors' represent the semantic space we are trying to detect
        anchor_phrases = [
            "I feel like I have no control over my life anymore.",
            "I am constantly in pain and want to stop existing.",
            "I started taking the pills again even though I promised I wouldn't."
        ]
        self.anchor_embeddings = self.model.encode(anchor_phrases, convert_to_tensor=True)
        self.threshold = 0.55 # Cosine similarity threshold for "High Risk"

    def detect(self, text: str) -> Tuple[float, List[float]]:
        """
        Input: Cleaned review string
        Output: Tuple of (Max semantic risk score, Raw text embedding vector)
        """
        # Encode the current review
        text_embedding = self.model.encode(text, convert_to_tensor=True)
        
        # Calculate cosine similarity against all anchor phrases
        cosine_scores = util.cos_sim(text_embedding, self.anchor_embeddings)
        
        # The risk score is the highest similarity to any of our anchor phrases
        max_score = cosine_scores.max().item()
        
        # Return the score and the raw vector (converted to list) for later clustering
        return max_score, text_embedding.tolist()


class PipelineOrchestrator:
    """Combines Rule-Based and Embedding-Based outputs into a final structured result."""
    def __init__(self):
        self.rule_detector = RuleDetector()
        self.embed_detector = EmbeddingDetector()

    def process_review(self, review: ProcessedReview) -> DetectionResult:
        """
        Input: ProcessedReview object
        Output: Final DetectionResult ready for temporal analysis
        """
        # 1. Run Rule-Based Check (Speed: Instant)
        substances, explicit_distress = self.rule_detector.detect(review.clean_text)
        
        # 2. Run Embedding Check (Speed: Fast, ~10-20ms per sentence locally)
        semantic_risk_score, vector = self.embed_detector.detect(review.clean_text)
        
        # 3. Aggregate Logic
        flags = []
        if explicit_distress:
            flags.append("explicit_relapse_or_distress")
        if semantic_risk_score >= self.embed_detector.threshold:
            flags.append("high_semantic_risk")
            
        # 2. Determine Emotional Tone (New logic for your schema)
        # We define distress as either an explicit keyword match OR high semantic similarity
        is_distressed = explicit_distress or (semantic_risk_score >= self.embed_detector.threshold)
        tone = "distress" if is_distressed else "neutral"
        
        # Boost risk score if both detectors trigger
        final_risk_score = semantic_risk_score
        if explicit_distress:
            final_risk_score = min(1.0, final_risk_score + 0.3)

        return DetectionResult(
            review_id=review.review_id,
            timestamp=review.date,
            drug_name=review.drug_name,
            condition=review.condition or "Unknown",
            detected_substances=substances,
            risk_score=round(final_risk_score, 3),
            emotional_tone=tone,      # Fixed: Added the missing required field
            flags=flags,
            embedding=vector # Save this for Phase 2 (Clustering/Behavioral Analysis)
        )
