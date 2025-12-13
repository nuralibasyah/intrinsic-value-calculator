import math


def graham_number(eps: float, book_value_per_share: float) -> float:
    return math.sqrt(22.5 * eps * book_value_per_share)
