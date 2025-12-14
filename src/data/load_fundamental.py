import pandas as pd

REQUIRED_COLUMNS = {
    "ticker",
    "year",
    "revenue",
    "net_income",
    "free_cash_flow",
    "eps",
    "book_value_per_share",
    "total_debt",
    "cash_and_equivalents",
    "shares_outstanding",
    "roe",
    "roic",
}


def load_fundamental(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    validate_fundamental_schema(df)
    return df


def validate_fundamental_schema(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
