import pandas as pd


def sensitivity_table(
    valuation_fn,
    base_params: dict,
    param_ranges: dict,
) -> pd.DataFrame:
    """
    param_ranges = {"growth_rate": [0.05, 0.07, 0.09]}
    """
    results = []

    for param, values in param_ranges.items():
        for v in values:
            params = base_params.copy()
            params[param] = v
            fv = valuation_fn(**params)
            results.append({param: v, "fair_value": fv})

    return pd.DataFrame(results)
