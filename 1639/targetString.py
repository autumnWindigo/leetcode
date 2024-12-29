import unittest

from typing import List

"""

base case: End of word reached, Word created

Skip: If wrong letter, actions: i + 1

Take: Find amount possible with each word. Add each possibility to ways.
        Move deeper into recursion for each of those ways
        actions: count + 1, i + 1

Memory: ? Just going to use @cache unless it's obnouxiously slow

"""

from functools import cache
from collections import defaultdict


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD_AMOUNT = 10**9 + 7

        # Precompute character counts for each word
        word_len = len(words[0])  # Length of each word
        char_count = [defaultdict(int) for _ in range(word_len)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][char] += 1

        @cache
        def numWays_from_index(index: int, target_index: int):
            # Base case: Created target
            if target_index == len(target):
                return 1

            # Base case: Hit end of word without creating target
            if index >= len(words[0]):
                return 0

            # Skip
            # Move index of words forwards
            ways = numWays_from_index(index + 1, target_index)

            # Take
            if target[target_index] in char_count[index]:
                ways += (
                    char_count[index][target[target_index]]
                    * numWays_from_index(index + 1, target_index + 1)
                ) % MOD_AMOUNT

            # Top Of Recursion
            return ways % MOD_AMOUNT

        return numWays_from_index(0, 0)


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        self.assertEqual(6, self.sol.numWays(["acca", "bbbb", "caca"], "aba"))

    def test_two(self):
        self.assertEqual(4, self.sol.numWays(["abba", "baab"], "bab"))

    def test_three(self):
        self.assertEqual(
            677452090,
            self.sol.numWays(
                [
                    "cbabddddbc",
                    "addbaacbbd",
                    "cccbacdccd",
                    "cdcaccacac",
                    "dddbacabbd",
                    "bdbdadbccb",
                    "ddadbacddd",
                    "bbccdddadd",
                    "dcabaccbbd",
                    "ddddcddadc",
                    "bdcaaaabdd",
                    "adacdcdcdd",
                    "cbaaadbdbb",
                    "bccbabcbab",
                    "accbdccadd",
                    "dcccaaddbc",
                    "cccccacabd",
                    "acacdbcbbc",
                    "dbbdbaccca",
                    "bdbddbddda",
                    "daabadbacb",
                    "baccdbaada",
                    "ccbabaabcb",
                    "dcaabccbbb",
                    "bcadddaacc",
                    "acddbbdccb",
                    "adbddbadab",
                    "dbbcdcbcdd",
                    "ddbabbadbb",
                    "bccbcbbbab",
                    "dabbbdbbcb",
                    "dacdabadbb",
                    "addcbbabab",
                    "bcbbccadda",
                    "abbcacadac",
                    "ccdadcaada",
                    "bcacdbccdb",
                ],
                "bcbbcccc",
            ),
        )


if __name__ == "__main__":
    unittest.main()
