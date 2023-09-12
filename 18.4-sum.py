#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List
# @lc code=start


class Solution:
    # time complexity: O(n^3)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # 必不合法
            if nums[i] > target and nums[i] > 0:
                break
            # 去重複
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                # 必不合法
                if nums[i] + nums[j] > target and nums[j] > 0:
                    break
                # 去重複
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # 2 sum
                [-2, -1, 0, 0, 1, 2]
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]])
                        # 跳過重複
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result

    # time complexity: O(n^3)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    # 避免重複使用同一個元素
                    if val in freq:
                        count = (nums[i] == val) + \
                            (nums[j] == val) + (nums[k] == val)
                        if freq[val] > count:
                            ans.add(
                                tuple(sorted([nums[i], nums[j], nums[k], val])))

        return [list(x) for x in ans]
# @lc code=end
