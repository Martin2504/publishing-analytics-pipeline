import pandas as pd
from pipeline.clean import clean_data

"""
Tests for data cleaning logic

Verifies that missing values and invalid data are handled correctly
during the cleaning stage of the pipeline.
"""

def test_clean_data_handles_missing_and_invalid_values():
    df = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "title": ["Book A", "Book B", "Book C", None],
        "author": ["Author A", None, "Author C", "Author D"],
        "sales": ["100", "abc", None, "300"]
    })

    cleaned_df =  clean_data(df)

    assert len(cleaned_df) == 3
    assert cleaned_df.loc[1, "author"] == "Unknown"
    assert cleaned_df.loc[1, "sales"] == 0
    assert cleaned_df.loc[2, "sales"] == 0
