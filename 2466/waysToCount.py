"""
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

    Append the character '0' zero times.
    Append the character '1' one times.

This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

===================

Desicions:
    Base Cases: Count goes above high
    Take: If count < high -> take count + zero & count + one



"""

import unittest
from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        @cache
        def countGoodStrings_fromCount(count: int) -> int:
            if count > high:
                return 0

            ways = countGoodStrings_fromCount(count + zero) + countGoodStrings_fromCount(count + one)
            if low <= count <= high:
                ways += 1

            return ways % MOD

        return countGoodStrings_fromCount(0)


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        self.assertEqual(self.sol.countGoodStrings(3, 3, 1, 1), 8)

    def test_two(self):
        self.assertEqual(self.sol.countGoodStrings(2, 3, 1, 2), 5)

    def test_three(self):
        self.assertEqual(self.sol.countGoodStrings(200, 200, 10, 1), 764262396)


if __name__ == '__main__':
    unittest.main()
