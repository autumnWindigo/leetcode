import unittest
# You are given an integer array values where values[i] represents the value of
# the ith sightseeing spot.
# Two sightseeing spots i and j have a distance j - i between them.
#
# The score of a pair (i < j) of
# sightseeing spots is values[i] + values[j] + i - j:
# the sum of the values of the sightseeing spots,
# minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.
#
#
# Example 1:
#
# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
#
# Example 2:
#
# Input: values = [1,2]
# Output: 2
#
#
# Constraints:
#
#     2 <= values.length <= 5 * 104
#     1 <= values[i] <= 1000


# values[i] + values[j] + i - j
# Val1  starts at values[0]
#       values[i] + values[j] + i - j

#       (values[i] + i) value of i

#       (values[j] - j) value of j

# Keep val1:    val1 > value[i] + i || i > j
# update val1: !keep


# Val2  starts at values[1] (?)

# Distance1
# Distance2

# Decisions ::
#   find new v2
#   update max_pair
#   if v1 + distance > max set v1
#
#
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        v1 = values[0] + 0
        max_pair = 0

        for i in range(1, len(values)):
            v2 = values[i] - i  # New v2 Value
            max_pair = max(max_pair, v1 + v2)  # If better with that new value
            v1 = max(v1, values[i] + i)  # If better with new v1

        return max_pair


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        self.assertEqual(11, self.sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]))

    def test_two(self):
        self.assertEqual(2, self.sol.maxScoreSightseeingPair([1, 2]))


if __name__ == '__main__':
    unittest.main()
