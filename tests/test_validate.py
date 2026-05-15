import pandas as pd
from pipeline.validate import validate_schema, validate_business_rules

"""
Tests for validation logic

Ensures schema and business rule validations behave correctly,
including handling invalid and edge-case data.
"""

def test_validate_schema_passes_with_required_columns():
    df = pd.DataFrame({
        "id": [1],
        "title": ["Book A"],
        "author": ["Author A"],
        "sales": [100.0]
    })

    result = validate_schema(df)

    assert result is not None

def test_validate_schema_fails_when_column_missing():
    df = pd.DataFrame({
        "id": [1],
        "title": ["Book A"],
        "sales": [100.0]
    })

    result = validate_schema(df)

    assert result is None

def test_validate_business_rules_passes_with_valid_data():
    df = pd.DataFrame({
        "id": [1],
        "title": ["Book A"],
        "author": ["Author A"],
        "sales": [100.0]
    })

    result = validate_business_rules(df)

    assert result is not None


def test_validate_business_rules_fails_when_id_not_numeric():
    df = pd.DataFrame({
        "id": ["abc"],
        "title": ["Book A"],
        "author": ["Author A"],
        "sales": [100.0]
    })

    result = validate_business_rules(df)

    assert result is None


def test_validate_business_rules_fails_when_id_missing():
    df = pd.DataFrame({
        "id": [None],
        "title": ["Book A"],
        "author": ["Author A"],
        "sales": [100.0]
    })

    result = validate_business_rules(df)

    assert result is None


def test_validate_business_rules_fails_when_title_empty():
    df = pd.DataFrame({
        "id": [1],
        "title": ["   "],
        "author": ["Author A"],
        "sales": [100.0]
    })

    result = validate_business_rules(df)

    assert result is None


def test_validate_business_rules_fails_when_author_empty():
    df = pd.DataFrame({
        "id": [1],
        "title": ["Book A"],
        "author": ["   "],
        "sales": [100.0]
    })

    result = validate_business_rules(df)

    assert result is None


def test_validate_business_rules_fails_when_sales_not_numeric():
    df = pd.DataFrame({
        "id": [1],
        "title": ["Book A"],
        "author": ["Author A"],
        "sales": ["abc"]
    })

    result = validate_business_rules(df)

    assert result is None

def test_validate_business_rules_fails_on_negative_sales():
    df = pd.DataFrame({
        "id": [1],
        "title": ["Book A"],
        "author": ["Author A"],
        "sales": [-10.0]
    })

    result = validate_business_rules(df)

    assert result is None
