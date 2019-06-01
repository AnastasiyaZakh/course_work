#!/usr/bin/env python
import unittest
from math import sqrt


def euler(n: int) -> int:
    phi = 1
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            n //= d
            phi *= d - 1
            while n % d == 0:
                n //= d
                phi *= d
    if n > 1:
        return phi * (n - 1)
    else:
        return phi


class TestEuler(unittest.TestCase):
    def test_1(self):
        self.assertEqual(euler(1), 1)

    def test_2(self):
        self.assertEqual(euler(2), 1)

    def test_3(self):
        self.assertEqual(euler(3), 2)

    def test_4(self):
        self.assertEqual(euler(4), 2)

    def test_5(self):
        self.assertEqual(euler(5), 4)

    def test_6(self):
        self.assertEqual(euler(6), 2)

    def test_7(self):
        self.assertEqual(euler(7), 6)

    def test_8(self):
        self.assertEqual(euler(8), 4)

    def test_9(self):
        self.assertEqual(euler(9), 6)

    def test_10(self):
        self.assertEqual(euler(10), 4)

    def test_9699690(self):
        self.assertEqual(euler(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19),
                         (2 - 1) * (3 - 1) * (5 - 1) * (7 - 1) * (11 - 1) * (13 - 1) * (17 - 1) * (19 - 1))

    def test_999961_999979(self):
        self.assertEqual(euler(999961 * 999979), (999961 - 1) * (999979 - 1))


if __name__ == '__main__':
    unittest.main()
