import fibonacci
import unittest


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci.fib(8), 13)
        self.assertEqual(fibonacci.fib(7), 8)
        self.assertEqual(fibonacci.fib(2), 1)
        self.assertEqual(fibonacci.fib(3), 1)
        self.assertEqual(fibonacci.fib(1), 0)


    def test_factorial(self):
        self.assertEqual(fibonacci.fact(1), 1)
        self.assertEqual(fibonacci.fact(2), 2)
        self.assertEqual(fibonacci.fact(3), 6)
        self.assertEqual(fibonacci.fact(5), 120)

if __name__ == "__main__":
    unittest.main()
