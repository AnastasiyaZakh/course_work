#!/usr/bin/env python
import unittest
from typing import Tuple
from extended_euclid import extended_euclid
from bin_pow_mod import bin_pow_mod


def rho_pollard_discrete_logarithm(g: int, p: int, t: int) -> int:
    a_0, b_0, x_0 = 0, 0, 1

    def step(a_i: int, b_i: int, x_i: int) -> Tuple[int, int, int]:
        if 0 <= x_i < p / 3:
            return (a_i + 1) % (p - 1), b_i % (p - 1), (t * x_i) % p
        if p / 3 <= x_i < 2 * p / 3:
            return (a_i << 1) % (p - 1), (b_i << 1) % (p - 1), (x_i * x_i) % p
        if 2 * p / 3 <= x_i < p:
            return a_i % (p - 1), (b_i + 1) % (p - 1), (g * x_i) % p

    a_i, b_i, x_i = step(a_0, b_0, x_0)
    a_2i, b_2i, x_2i = step(*step(a_0, b_0, x_0))

    while x_i != x_2i:
        a_i, b_i, x_i = step(a_i, b_i, x_i)
        a_2i, b_2i, x_2i = step(*step(a_2i, b_2i, x_2i))

    # (a_2i - a_i) * k = b_i - b_2i (mod p - 1)

    d, x, y = extended_euclid(a_2i - a_i, p - 1)

    if d == 1:
        return x % (p - 1)
    else:
        x_0 = x * d
        for m in range(d):
            if bin_pow_mod(g, x_0 + m * (p - 1) // d, p) == t:
                return x_0 + m * (p - 1) // d


class TestRhoPollardDiscreteLogarithm(unittest.TestCase):
    def test(self):
        self.assertEqual(rho_pollard_discrete_logarithm(3, 43, 15), 26)


if __name__ == '__main__':
    unittest.main()
