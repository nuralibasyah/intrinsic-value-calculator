import numpy as np
import math


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


def per_valuation(eps: float, fair_per: float = 15) -> float:
    return eps * fair_per


def pbv_valuation(book_value_per_share: float, fair_pbv: float = 1.5) -> float:
    return book_value_per_share * fair_pbv


def graham_number(eps: float, book_value_per_share: float) -> float:
    return math.sqrt(22.5 * eps * book_value_per_share)


def calc_dcf_iv(
    row, growth_rate=0.08, discount_rate=0.12, terminal_growth=0.03, years=5
) -> float:
    return dcf_intrinsic_value(
        fcf=row["free_cash_flow(ttm)"],
        growth_rate=growth_rate,
        discount_rate=discount_rate,
        terminal_growth=terminal_growth,
        years=years,
        shares_outstanding=row["shares_outstanding"],
    )


def calc_per_iv(row, fair_per: float = 10) -> float:
    return per_valuation(eps=row["eps(ttm)"], fair_per=fair_per)


def calc_graham_iv(row):
    return graham_number(
        eps=row["eps(ttm)"], book_value_per_share=row["book_value_per_share"]
    )


def calc_pbv_iv(row, fair_pbv: float = 1.5) -> float:
    return pbv_valuation(
        book_value_per_share=row["book_value_per_share"], fair_pbv=fair_pbv
    )
