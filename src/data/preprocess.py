import pandas as pd


def compute_fcf_growth(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("year").copy()
    df["fcf_growth"] = df["free_cash_flow"].pct_change()
    return df


def normalize_units(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure numeric columns are floats (defensive)."""
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].astype(float)
    return df
