#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start


class Solution:
    # 第一個想法，時間複雜度 O(n^2)，且會有重複問題
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if target - num in nums:
                return [nums.index(num), nums.index(target - num)]
        return False

    # 使用dict存看過的數字
    # 時間複雜度 O(n)
    # 空間複雜度 O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = {}
        for index, value in enumerate(nums):
            # in dict的時間複雜度是 O(1)
            if target - value in records:
                return [records[target - value], index]
            records[value] = index
        return []

    # 雙指針
    # 時間複雜度 O(nlogn)
    # 空間複雜度 O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        left = 0
        right = len(nums_sorted) - 1
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right])
                if left_index == right_index:  # 數字相同，回傳第一個index(比較小的)
                    right_index = nums[left_index +
                                       1:].index(nums_sorted[right]) + left_index + 1
                return [left_index, right_index]
            elif current_sum < target:
                # 如果总和小于目标，则将左侧指针向右移动
                left += 1
            else:
                # 如果总和大于目标值，则将右指针向左移动
                right -= 1
# @lc code=end

test_list = [1, 2, 3, 12, 5, 6, 17, 10, 5]
print(test_list[4+1:])  # [6, 17, 10, 5]