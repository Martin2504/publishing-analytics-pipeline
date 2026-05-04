import pandas as pd

""" 
Ingestion Module

This module is responsible for loading raw data into the pipeline.
It provides functionality to read CSV files and handle common ingestion errors.

Responsibilities:
- Load data from CSV files
- Provide basic validation of file accessibility
- Handle ingestion-related errors gracefully
- Output useful debugging information (e.g. row count, shape)

This is the first stage of the data pipeline:
Ingest → Clean → Validate → Store → Expose (API)
"""

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding="utf-8")

        print(f"[INFO] Successfully loaded data from {file_path}")
        print(f"[INFO] Shape: {df.shape}")
        print(f"[INFO] Row count: {len(df)}")

        return df

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None
    
    except pd.errors.EmptyDataError:
        print(f"[ERROR] File is empty: {file_path}")
        return None
    
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return None