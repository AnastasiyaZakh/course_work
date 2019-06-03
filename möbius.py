#!/usr/bin/env python
import unittest
from math import sqrt


def möbius(n: int) -> int:
    mu = 1
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            n //= d
            mu *= -1
            if n % d == 0:
                return 0

    if n > 1:
        return -mu
    else:
        return mu


class TestMöbius(unittest.TestCase):
    def test_1(self):
        self.assertEqual(möbius(1), 1)

    def test_2(self):
        self.assertEqual(möbius(2), -1)

    def test_3(self):
        self.assertEqual(möbius(3), -1)

    def test_4(self):
        self.assertEqual(möbius(4), 0)

    def test_5(self):
        self.assertEqual(möbius(5), -1)

    def test_6(self):
        self.assertEqual(möbius(6), 1)

    def test_7(self):
        self.assertEqual(möbius(7), -1)

    def test_8(self):
        self.assertEqual(möbius(8), 0)

    def test_9(self):
        self.assertEqual(möbius(9), 0)

    def test_10(self):
        self.assertEqual(möbius(10), 1)

    def test_9699690(self):
        self.assertEqual(möbius(9699690), 1)

    def test_999961_999979(self):
        self.assertEqual(möbius(999961 * 999979), 1)


if __name__ == '__main__':
    unittest.main()
