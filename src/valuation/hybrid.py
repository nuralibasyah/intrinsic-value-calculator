def weighted_fair_value(values: dict, weights: dict) -> float:
    if set(values.keys()) != set(weights.keys()):
        raise ValueError("Values and weights must have same keys")

    return sum(values[k] * weights[k] for k in values)
