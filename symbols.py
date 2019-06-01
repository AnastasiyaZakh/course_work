#!/usr/bin/env python
import unittest
from typing import Tuple
from extended_euclid import extended_euclid
from cmath import sqrt
from rho_pollard_fact import rho_pollard


def legendre(a, b):

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

    return(int(leg * sign))

def jacobi(a, b):
    p = []
    jac = 1
    for factor in rho_pollard(b):
        p.append(factor)

    for p_i in p:
        jac *= legendre(a, p_i)

    return jac
        # if not extended_euclid(a, b)[0] == 1:
        #     return 0
        # r = 1
        # if a < 0:
        #     a = -a
        #     if b % 4 == 3:
        #         r = -r
        # while True:
        #     t = 0
        #     while a % 2 == 0:
        #         t = t + 1
        #         a = a / 2
        #
        #     if not t % 2 == 0:
        #         if b % 8 == 3 or b % 8 == 5:
        #             r = -r
        #
        #     if a % 4 == b % 4 == 3:
        #         r = -r
        #     c = a
        #     a = b % c
        #     b = c
        #     if a == 0:
        #         break
        #     else:
        #         return r


    # return legendre(a, b), jacobi(a, b)


class TestSymbols(unittest.TestCase):
    def test_1(self):
        self.assertEqual(legendre(45, 113), (-1))

    def test_2(self):
        self.assertEqual(jacobi(3, 29), (-1))

    def test_3(self):
        self.assertEqual(jacobi(3, 654), (0))


if __name__ == '__main__':
    unittest.main()
