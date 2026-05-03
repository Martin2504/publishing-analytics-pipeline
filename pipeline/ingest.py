import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)

        print(f"[INFO] Successfully loaded data from {file_path}")
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