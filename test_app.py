"""Unit tests for the sample utility module."""

import unittest

from app import add, is_even, multiply, subtract


class TestApp(unittest.TestCase):
    """Test cases for app.py utility functions."""

    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 99), 0)

    def test_is_even(self) -> None:
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))
        


if __name__ == "__main__":
    unittest.main()

