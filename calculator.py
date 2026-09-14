def divide(numerator: float, denominator: float) -> float:
    """Divide two numbers. Denominator must not be zero."""
    if denominator == 0:
        raise ValueError("Denominator must not be zero")
    return numerator / denominator

def add(a: float, b: float) -> float:
    """Add two floating point numbers and return the result."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a (a - b) with floating point numbers and return the result."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two floating point numbers and return the result."""
    return a * b
