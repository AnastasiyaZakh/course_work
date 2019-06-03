#!/usr/bin/env python
from extended_euclid import extended_euclid
from typing import Tuple
from math import sqrt
import unittest


def _rho_pollard(number: int):
    answer = set()
    print(number)
    for d in range(2, min(int(sqrt(sqrt(number))) + 10, number)):
        if number % d == 0:
            answer.add(d)
        while number % d == 0:
            number //= d

    if number == 1:
        return answer

    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1

    while factor == 1:
        count = 1
        while count <= cycle_size and factor <= 1:
            x = (x * x + 1) % number
            factor = abs(extended_euclid(x - x_fixed, number)[0])
            count += 1
        cycle_size *= 2
        x_fixed = x

    if factor == number:
        return {factor} | answer
    else:
        return {factor} | rho_pollard(number // factor) | answer


def rho_pollard(number: int):
    factors = _rho_pollard(number)
    # return factors
    factor_powers = {}

    for factor in factors:
        while number % factor == 0:
            factor_powers[factor] = factor_powers.get(factor, 0) + 1
            number //= factor

    sl = []
    for factor, power in factor_powers.items():
        sl.append(f'{factor}^{power}')
    print(factors)
    return factor_powers, ' * '.join(sl)


class TestRhoPollardFact(unittest.TestCase):
    def test_1(self):
        self.assertEqual(_rho_pollard(168), {2, 3, 7})


if __name__ == '__main__':
    unittest.main()
