def divide(numerator: float, denominator: float) -> float:
    """Divide two numbers. Denominator must not be zero."""
    if denominator == 0:
        raise ValueError("Denominator must not be zero")
    return numerator / denominator
