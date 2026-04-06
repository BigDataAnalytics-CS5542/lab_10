import pandas as pd
from typing import Iterator, List
from src.schemas import RawReview

def load_uci_dataset(file_path: str) -> pd.DataFrame:
    """
    Loads the Kaggle UCI dataset, handling its specific date format 
    and dropping unparseable rows.
    """
    # The UCI dataset uses string dates like "12-Aug-08"
    df = pd.read_csv(file_path)
    
    # Fast datetime conversion
    df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y', errors='coerce')
    
    # Drop rows where essential data is missing
    df = df.dropna(subset=['review', 'date'])
    return df

def stream_batches(df: pd.DataFrame, batch_size: int = 500) -> Iterator[List[RawReview]]:
    """
    Yields batches of validated Pydantic objects.
    """
    batch = []
    i = 0
    for record in df.to_dict(orient="records"):
        try:
            # Validate and map to Pydantic model
            review = RawReview(**record)
            batch.append(review)
            
            if len(batch) >= batch_size:
                yield batch
                batch = []
        except Exception as e:
            if i < 5:
                print(f"Validation error on row {i}: {e}")
            # Log validation errors if necessary; skip malformed row
            continue
        finally:
            i+=1
            
    if batch:
        yield batch