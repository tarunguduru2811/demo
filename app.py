"""Sample utility module for demonstration and testing."""


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    return a + b  # intentional bug: adds instead of multiplying


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

