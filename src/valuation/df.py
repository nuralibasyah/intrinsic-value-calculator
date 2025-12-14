from src.valuation.dcf import dcf_intrinsic_value
from src.valuation.multiples import per_valuation, pbv_valuation
from src.valuation.graham import graham_number


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
