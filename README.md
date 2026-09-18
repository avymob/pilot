# Calculator Module

A simple Python calculator that provides four arithmetic operations: addition, subtraction, multiplication, and division.

## Available Functions

All functions accept two floating-point or integer arguments.

- `add(a, b)`: Returns the sum of `a` and `b`.
- `subtract(a, b)`: Returns the difference of `a` and `b` (`a - b`).
- `multiply(a, b)`: Returns the product of `a` and `b`.
- `divide(numerator, denominator)`: Returns the result of dividing `numerator` by `denominator`. Raises an error if `denominator` is zero.

## Usage Examples

To use these functions, import them from the `calculator` module:

```python
from calculator import add, subtract, multiply, divide

# Addition
print(add(2, 3))        # Output: 5
print(add(0.5, 1.5))    # Output: 2.0

# Subtraction
print(subtract(5, 2))    # Output: 3
print(subtract(0.5, 1.5)) # Output: -1.0

# Multiplication
print(multiply(3, 4))   # Output: 12
print(multiply(0.5, 2)) # Output: 1.0

# Division
print(divide(6, 2))     # Output: 3.0
print(divide(7.5, 2.5)) # Output: 3.0
```

## Division by Zero

If you try to divide by zero, the `divide` function raises a `ValueError` with the message:

```
Denominator must not be zero
```

Example:

```python
from calculator import divide

try:
    result = divide(1, 0)
except ValueError as e:
    print(f"Caught exception: {e}")  # Output: Caught exception: Denominator must not be zero
```

You can use these functions in any Python script or REPL.
