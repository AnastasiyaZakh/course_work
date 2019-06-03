#!/usr/bin/env python
import unittest
from typing import Tuple
from extended_euclid import extended_euclid
from cmath import sqrt
from rho_pollard_fact import _rho_pollard


def legendre(a: int, b: int) -> int:
    leg = 5
    sign = 1
    while a != -1 and sqrt(a) ** 2 != a:
        if a % b == 0: leg = 0; break
        if a < b:
            a, b = b, a
            sign *= (-1) ** ((a - 1) / 2 * (b - 1) / 2)
        if (a % b) % 2 == 0:
            a -= b * (a // b + 1)
        else:
            a %= b

    # a = 1 или -1 or sqrt is int
    if a == 1 or isinstance(sqrt(a), int):
        leg = 1
    elif a == -1:
        leg = 1 if b % 4 == 1 else -1

    return int(leg * sign)


def jacobi(a: int, b: int) -> int:
    p = []
    jac = 1
    for factor in _rho_pollard(b):
        p.append(factor)

    for p_i in p:
        jac *= legendre(a, p_i)

    return jac


class TestSymbols(unittest.TestCase):
    def test_1(self):
        self.assertEqual(legendre(45, 113), (-1))



if __name__ == '__main__':
    unittest.main()
