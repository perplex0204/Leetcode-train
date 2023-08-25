#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

from typing import List

# @lc code=start


class Solution:
    # 第一個想法
    # time: O(n * n+m) # set() is O(N)
    # space: O(n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in set(nums1):
            if num in nums2:
                result.append(num)
        return result

    # GPT
    # time: O(n+m)
    # space: O(n+m)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    # python sol
    # intersection: 兩個set的交集
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)
# @lc code=end
