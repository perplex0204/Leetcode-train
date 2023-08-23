# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.md
#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start

"""
python3 作弊法
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([num ** 2 for num in nums])


"""
Accepted
137/137 cases passed (182 ms)
Your runtime beats 99.55 % of python3 submissions
Your memory usage beats 46.63 % of python3 submissions (18.6 MB)
"""


"""
雙指針法
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums)  # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:  # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1  # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1  # 左指针往右移动
            i -= 1  # 存放结果的指针需要往前平移一位
        return res


"""
Accepted
137/137 cases passed (242 ms)
Your runtime beats 39.95 % of python3 submissions
Your memory usage beats 5.04 % of python3 submissions (18.8 MB)
"""

# @lc code=end
