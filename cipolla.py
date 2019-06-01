#!usr/bin/env python
import unittest
from symbols import legendre

def cipolla(a: int, p: int):
    if legendre(a, p) == -1:
        return 'Немає розв*язку'
    elif legendre(a, p) == 1:
        for t in range(0, p-1):
            v = t ** 2 - a
            if legendre(v, p) == -1:
                break
            


class TestCipolla(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cipolla(), False)

if __name__ == '__main__':
    unittest.main()

