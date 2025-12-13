def per_valuation(eps: float, fair_per: float = 15) -> float:
    return eps * fair_per


def pbv_valuation(book_value_per_share: float, fair_pbv: float = 1.5) -> float:
    return book_value_per_share * fair_pbv
