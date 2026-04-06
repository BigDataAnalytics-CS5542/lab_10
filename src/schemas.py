from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Optional
from datetime import datetime

class RawReview(BaseModel):
    """Schema for the incoming raw UCI dataset row."""
    model_config = ConfigDict(populate_by_name=True)

    # Match the Kaggle "uniqueID" header
    review_id: int = Field(alias="uniqueID") 
    drug_name: str = Field(alias="drugName")
    condition: Optional[str] = None
    review: str
    rating: float
    date: datetime
    useful_count: int = Field(alias="usefulCount")

class ProcessedReview(RawReview):
    """Schema after text cleaning. Inherits the config from RawReview automatically."""
    clean_text: str

class DetectionResult(BaseModel):
    """Final output schema ready for temporal/behavioral analysis."""
    model_config = ConfigDict(populate_by_name=True)
    
    review_id: int
    timestamp: datetime
    drug_name: str
    condition: str
    detected_substances: List[str]  # e.g., ["opioids", "alcohol"]
    emotional_tone: str            # e.g., "distress", "neutral"
    risk_score: float              # 0.0 to 1.0
    embedding: Optional[List[float]] = None # For future clustering

