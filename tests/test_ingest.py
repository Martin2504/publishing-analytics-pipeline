from pipeline.ingest import load_data

"""
Tests for data ingestion logic

Verifies that CSV files are loaded correctly and that error handling
works as expected when files are missing or invalid.
"""

def test_load_data_success():
    df = load_data("data/raw/books_messy.csv")

    assert df is not None
    assert not df.empty

def test_load_data_file_not_found():
    df = load_data("data/raw/non_existent.csv")

    assert df is None