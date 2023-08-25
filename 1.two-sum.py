#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if target - num in nums:
                return [nums.index(num), nums.index(target - num)]
        return False
# @lc code=end
