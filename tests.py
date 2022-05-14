import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0_debe_devolver_0(self):
        self.assertEqual(fibonacci(0), 0, "fibonacci(0) debe devolver 0")

    def test_fibonacci_1_debe_devolver_1(self):
        self.assertEqual(fibonacci(1), 1, "fibonacci(1) debe devolver 1")

    def test_fibonacci_9_debe_devolver_34(self):
        self.assertEqual(fibonacci(9), 34, "fibonacci(9) debe devolver 34")


if __name__ == "__main__":
    unittest.main()
