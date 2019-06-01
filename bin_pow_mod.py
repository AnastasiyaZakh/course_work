#!/usr/bin/env python
import unittest


def bin_pow_mod(n: int, p: int, m: int) -> int:
    # n^p (mod m)
    if p == 0:
        return 1
    return ((n if p & 1 else 1) * bin_pow_mod((n * n) % m, p >> 1, m)) % m


class TestBinPowMod(unittest.TestCase):
    def test(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
