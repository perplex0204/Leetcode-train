# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md
#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start


# sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        sum = 0
        min_length = len(nums) + 1

        while right < len(nums):
            sum += nums[right]
            right += 1

            while sum >= target:
                min_length = min(min_length, right - left)
                sum -= nums[left]
                left += 1

        return min_length if min_length != len(nums) + 1 else 0
# @lc code=end


sol = Solution()
print(sol.minSubArrayLen(11, [1, 2, 3, 4, 5]))
