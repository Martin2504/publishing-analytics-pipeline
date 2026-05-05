import pandas as pd

"""
Data Cleaning Module

Handles transformation of raw data into a clean, usable format.

Responsibilities:
- Handle missing values
- Convert data types
- Standardise dataset for downstream processing
"""

def clean_data(df):

    print(f"[INFO] Cleaning data...")
    print(f"[INFO] Rows before cleaning: {len(df)}")

    # Drop rows where title is missing
    df = df.dropna(subset=['title']).copy()  # Use copy to avoid SettingWithCopyWarning

    # Fill missing authors
    df['author'] = df['author'].fillna('Unknown')

    # Convert sales to numeric (invalid values become NaN)
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

    # Fill missing sales with 0
    df['sales'] = df['sales'].fillna(0)

    # Standardise text fields
    df["title"] = df["title"].str.strip().str.title()
    df["author"] = df["author"].str.strip().str.title()

    print(f"[INFO] Rows after cleaning: {len(df)}")

    return df