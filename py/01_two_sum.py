#!/usr/bin/env python3

"""Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.


Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""


from typing import List


class Solution:
    """Solution for the classic two sum leet code problem."""

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """Given a number list and a target, return the indices of the two
        elements such their sum equals the target. In other words:

            nums[a] + nums[b] = target.

        The space and time complexity are in O(n).

        """
        memory = {}
        for index, item in enumerate(nums):
            if item in memory:
                return [index, memory[item]]
            memory[target - item] = index
