"""Convenience functions for working with Pandas DataFrame objects."""

import pandas as pd


def optimize_floats(df: pd.DataFrame) -> pd.DataFrame:
    """Reduces memory usage of floats in Pandas DataFrames.

    Reduces bit-width of integer columns in df if the full bit-width is not in use.

    Args:
        df: A Pandas DataFrame containing zero or more columns with dtype float64.

    Returns:
        The modified DataFrame
    """
    floats = df.select_dtypes(include=['float64']).columns.tolist()
    df[floats] = df[floats].apply(pd.to_numeric, downcast='float')
    return df


def optimize_ints(df: pd.DataFrame) -> pd.DataFrame:
    """Reduces memory usage of ints in Pandas DataFrames.

    Reduces bit-width of integer columns in df if the full bit-width is not in use.

    Args:
        df: A Pandas DataFrame containing zero or more columns with dtype int64.

    Returns:
        The modified DataFrame
    """
    ints = df.select_dtypes(include=['int64']).columns.tolist()
    df[ints] = df[ints].apply(pd.to_numeric, downcast='integer')
    return df


def rename_columns(df: pd.DataFrame, columns: dict) -> pd.DataFrame:
    """Rename columns in df using mapping in columns dict."""
    columns = {columns[k]: k for k in columns.keys()}
    df = df.rename(columns=columns)
    return df
