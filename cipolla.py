#!usr/bin/env python
import unittest
from symbols import legendre


def cipolla(a: int, p: int) -> str:
    if legendre(a, p) == -1:
        return 'Немає розв*язку'
    elif legendre(a, p) == 1:
        for t in range(1, p-1):
            v = t ** 2 - a
            if legendre(v, p) == -1:
                break
        y = 1
        t1, y1 = t, y
        for power in range(1, int((p+1)/2)):
            t1, y1 = (t1 * t + y1 * y * v) % p, (t1 * y + t * y1) % p
    return f'x = ±{t1}'


class TestCipolla(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cipolla(2, 17), 'x = ±6')


if __name__ == '__main__':
    unittest.main()
