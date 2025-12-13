import numpy as np


def dcf_intrinsic_value(
    fcf: float,
    growth_rate: float,
    discount_rate: float,
    terminal_growth: float,
    years: int,
    shares_outstanding: float,
) -> float:
    if discount_rate <= terminal_growth:
        raise ValueError("Discount rate must be greater than terminal growth")

    cash_flows = [fcf * (1 + growth_rate) ** t for t in range(1, years + 1)]

    discounted = [
        cf / (1 + discount_rate) ** t for t, cf in enumerate(cash_flows, start=1)
    ]

    terminal_value = (cash_flows[-1] * (1 + terminal_growth)) / (
        discount_rate - terminal_growth
    )

    terminal_discounted = terminal_value / (1 + discount_rate) ** years

    equity_value = sum(discounted) + terminal_discounted
    return equity_value / shares_outstanding
