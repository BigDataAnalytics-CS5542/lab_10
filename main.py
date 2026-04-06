import pandas as pd
import numpy as np
import time
import os

# Assuming your project structure matches the previously defined src/ layout
from src.loader import load_uci_dataset, stream_batches
from src.preprocessor import FastPreprocessor
from src.detection.engine import PipelineOrchestrator

def run_pipeline(input_csv_path: str, output_csv_path: str, embeddings_path: str):
    print(f"Loading raw data from {input_csv_path}...")
    df = load_uci_dataset(input_csv_path)
    
    # Initialize components once to avoid overhead
    preprocessor = FastPreprocessor()
    orchestrator = PipelineOrchestrator()
    
    all_results = []
    all_embeddings = []
    review_ids = []
    
    print("Starting batch processing...")
    start_time = time.time()
    
    # Stream in batches to keep memory usage low
    batch_size = 500
    for i, batch in enumerate(stream_batches(df, batch_size=batch_size)):
        
        # 1. Clean the text using compiled regex
        processed_batch = preprocessor.process_batch(batch)
        
        # 2. Run the Hybrid Detection Engine
        for review in processed_batch:
            result = orchestrator.process_review(review)
            
            # Extract dictionary representation for saving
            result_dict = result.model_dump()
            
            # Pop the embedding out so it doesn't clutter the CSV
            embedding = result_dict.pop('embedding')
            
            # Store data
            all_results.append(result_dict)
            all_embeddings.append(embedding)
            review_ids.append(result.review_id)
            
        # Optional progress tracking
        if (i + 1) % 10 == 0:
            print(f"Processed {(i + 1) * batch_size} records...")
            
    print(f"Detection complete in {time.time() - start_time:.2f} seconds.")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
  
    # 3. Save Tabular Results to CSV
    print(f"Saving structured signals to {output_csv_path}...")
    results_df = pd.DataFrame(all_results)
    results_df.to_csv(output_csv_path, index=False)
    
    # 4. Save Embeddings for Phase 2 (Clustering/Behavioral Analysis)
    print(f"Saving compressed embeddings to {embeddings_path}...")
    np.savez_compressed(
        embeddings_path, 
        review_ids=np.array(review_ids), 
        embeddings=np.array(all_embeddings)
    )
    
    print("Pipeline execution finished successfully.")

if __name__ == "__main__":
    # Define your paths here
    INPUT_FILE = "data/raw/drugsComTrain_raw.csv"
    OUTPUT_CSV = "data/processed_signals.csv"
    EMBEDDINGS_FILE = "data/embeddings.npz"
    
    run_pipeline(INPUT_FILE, OUTPUT_CSV, EMBEDDINGS_FILE)