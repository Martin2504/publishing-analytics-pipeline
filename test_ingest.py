from pipeline.ingest import load_data
from pipeline.clean import clean_data
from pipeline.validate import validate_schema, validate_business_rules

if __name__ == "__main__":

    # df = load_data("data/raw/books_clean.csv")  # This file contains cleaned book data, should load successfully
    # df = load_data("data/raw/missing.csv")  # This file does not exist, should trigger error handling
    df = load_data("data/raw/books_messy.csv") # This file contains messy data. Should load with NaNs and potential parsing issues, but should not crash the program

    if df is not None:
        # 1. Validate schema first
        df = validate_schema(df)

        if df is not None:
            # 2. Clean data
            df = clean_data(df)

            #3. Validate business rules
            df = validate_business_rules(df)

            if df is not None:
                print("\n[INFO] Final Valid Data:")
                print(df.head())

                df.to_csv("data/processed/books_cleaned.csv", index=False)
                print("\n[INFO] Cleaned data saved to data/processed/books_cleaned.csv")