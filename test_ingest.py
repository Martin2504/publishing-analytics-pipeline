from pipeline.ingest import load_data

if __name__ == "__main__":

    df = load_data("data/raw/books.csv")
    # df = load_data("data/raw/missing.csv")  # This file does not exist, should trigger error handling

    if df is not None:
        print(df.head())
        print(f"Row count: {len(df)}")