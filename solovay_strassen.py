#!/usr/bin/env python
import unittest
from random import randrange
from extended_euclid import extended_euclid
from symbols import jacobi


def solovay_strassen(n: int, k: int) -> str:
    for i in range(1, k + 1):
        a = int(randrange(2, n - 1))
        if extended_euclid(a, n)[0] > 1:
            return "Складене"
        elif not (a ** ((n-1)/2)) % n == jacobi(a, n) % n:
            return "Складене"
        else:
            "Просте"  # з ймовірністю 1 - 2^{-k}


class TestSolovayStrassen(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solovay_strassen(1145, 2), "Просте")

    def test_2(self):
        self.assertEqual(solovay_strassen(4, 2), "Складене")


if __name__ == '__main__':
    unittest.main()
