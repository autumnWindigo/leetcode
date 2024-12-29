"""
Given an integer array nums and an integer k, find three non-overlapping
subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of
each interval (0-indexed). If there are multiple answers,
return the lexicographically smallest one.


Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to
the starting indices [0, 3, 5].

We could have also taken [2, 1], but an answer of [1, 3, 5]
would be lexicographically larger.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]


Constraints:

    1 <= nums.length <= 2 * 104
    1 <= nums[i] < 216
    1 <= k <= floor(nums.length / 3)

=====================

Decision:
How do we start?
Find 3 subbarrays which have maximum sum in array

Take ith subarray
    - have to set index of max subarray to ith subarray

Skip ith subarry
    - have to move to ith+1 index

Recursive calls:
    Base Case: If no subbarrays left to pick or we hit the end of array

    Skip: Move onto next subarray (start + 1)

    Take: Take current subarray and add it's sum to result
            then move onto next non-overlapping subarray

    Compare: Find which is sum is greater then which is lexigraphically better

    Memory: Save both results in memory
"""

import unittest
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Precompute the summation of all possible subarrays
        subarray_sums = [sum(nums[i: i + k]) for i in range(len(nums) - k + 1)]

        # Memory for caching inside recursive calls
        memory = {}

        def find_maxSubarrays(count: int, start: int) -> (int, List[int]):
            # Base Case: If all subarrays are found
            if count == 0:
                return 0, []

            # Base Case: If end of array is reached
            if start >= len(subarray_sums):
                return float("-inf"), []

            # Check if recursive run is in memory
            if (count, start) in memory:
                return memory[(count, start)]

            # SKIP
            # We need to save the skips
            skip_sum, skip_indices = find_maxSubarrays(count, start + 1)

            # TAKE
            # Take and move count
            chosen_sum, chosen_indices = find_maxSubarrays(count - 1, start + k)
            chosen_sum += subarray_sums[start]

            if chosen_sum > skip_sum:
                # Append chosen indeces to the list
                result = (chosen_sum, [start] + chosen_indices)
            elif chosen_sum < skip_sum:
                # Skip save for caching
                result = (skip_sum, skip_indices)
            else:  # if they're equal
                # Take if chosen is lexigraphically better
                if [start] + chosen_indices < skip_indices:
                    result = (chosen_sum, [start] + chosen_indices)
                # Otherwise skip
                else:
                    result = (skip_sum, skip_indices)

            # Add results to memory
            memory[(count, start)] = result
            return result

        _, result = find_maxSubarrays(3, 0)
        return result


# Tests
class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        self.assertEqual(
            self.sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2), [0, 3, 5]
        )

    def test_two(self):
        self.assertEqual(
            self.sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2), [0, 2, 4]
        )


if __name__ == "__main__":
    unittest.main()
