# !/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def _rho_pollard(number):
    answer = set()
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
            factor = gcd(x - x_fixed, number)
            count += 1
        cycle_size *= 2
        x_fixed = x

    if factor == number:
        return {factor} | answer
    else:
        return {factor} | rho_pollard(number // factor) | answer


def rho_pollard(number):

    factors = _rho_pollard(number)
    factors_all = []

    for factor in factors:
        while number % factor == 0:
            factors_all.append(factor)
            number /= factor
    return factors_all

    # factor_powers = {}
    #
    # for factor in factors:
    #     while number % factor == 0:
    #         factor_powers[factor] = factor_powers.get(factor, 0) + 1
    #         number //= factor
    #
    # sl = []
    # for factor, power in factor_powers.items():
    #     sl.append(f'{factor}^{power}')
    # print (factors)
    # return factor_powers, ' * '.join(sl)


print(rho_pollard(1588))

