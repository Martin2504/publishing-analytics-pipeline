import pandas as pd

"""
Validation Module

Ensures that cleaned data meets required schema and business rules
before being stored or exposed via the API.
"""

def validate_schema(df):
    print("[INFO] Validating schema...")

    # Requireed Schema
    required_columns = ['id', 'title', 'author', 'sales']

    # 1. Check required columns exist
    for col in required_columns:
        if col not in df.columns:
            print(f"[ERROR] Missing required column: {col}")
            return None

    # 2. Check for empty DataFrame 
    if df.empty:
        print("[ERROR] DataFrame is empty")
        return None

    print("[INFO] Schema validation passed")
    return df


def validate_business_rules(df):
    print("[INFO] Validating business rules...")

    # 1. Check sales are numeric
    if not pd.api.types.is_numeric_dtype(df['sales']):
        print("[ERROR] Sales column is not numeric")
        return None

    # 2. Check for negative sales
    if (df['sales'] < 0).any():
        print("[ERROR] Negative sales values found")
        return None
    
    print(f"[INFO] Rows validated: {len(df)}")

    print("[INFO] Business rules validation passed")
    return df

