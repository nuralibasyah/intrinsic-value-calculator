def margin_of_safety(fair_value: float, market_price: float) -> float:
    return (fair_value - market_price) / fair_value
