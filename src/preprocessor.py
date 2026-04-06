import re
from typing import List
from src.schemas import RawReview, ProcessedReview

class FastPreprocessor:
    def __init__(self):
        # Compile regex for speed
        self.html_cleaner = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        self.special_chars = re.compile(r'[^a-zA-Z0-9\s.,!?]')
        self.multiple_spaces = re.compile(r'\s+')

    def clean_text(self, text: str) -> str:
        """Applies regex-based cleaning to standard review text."""
        text = text.lower()
        text = self.html_cleaner.sub(' ', text)
        text = self.special_chars.sub('', text)
        text = self.multiple_spaces.sub(' ', text).strip()
        return text

    def process_batch(self, batch: List[RawReview]) -> List[ProcessedReview]:
        """Processes a batch of raw reviews into clean reviews."""
        processed_batch = []
        for review in batch:
            clean_str = self.clean_text(review.review)
            
            # Create new ProcessedReview, inheriting data from RawReview
            processed_review = ProcessedReview(
                **review.model_dump(),
                clean_text=clean_str
            )
            processed_batch.append(processed_review)
            
        return processed_batch