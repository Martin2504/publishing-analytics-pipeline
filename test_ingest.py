from pipeline.ingest import load_data
from pipeline.clean import clean_data

if __name__ == "__main__":

    # df = load_data("data/raw/books_clean.csv")  # This file contains cleaned book data, should load successfully
    # df = load_data("data/raw/missing.csv")  # This file does not exist, should trigger error handling
    df = load_data("data/raw/books_messy.csv") # This file contains messy data. Should load with NaNs and potential parsing issues, but should not crash the program

    if df is not None:
        cleaned_df = clean_data(df)

        print("\n[INFO] Cleaned Data:")
        print(cleaned_df.head())