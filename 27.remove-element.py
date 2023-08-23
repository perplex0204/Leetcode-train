# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.md
#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start

"""
python作弊法
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            print(nums)
        return len(nums)
"""
Accepted
113/113 cases passed (38 ms)
Your runtime beats 96.77 % of python3 submissions
Your memory usage beats 72.72 % of python3 submissions (16.3 MB)
"""

"""
暴力解
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val:  # 找到等于目标值的节点
                for j in range(i+1, l):  # 移除该元素，并将后面元素向前平移
                    nums[j - 1] = nums[j]
                l -= 1
                i -= 1
            i += 1
        return l
"""
Accepted
113/113 cases passed (36 ms)
Your runtime beats 98.06 % of python3 submissions
Your memory usage beats 38.51 % of python3 submissions (16.3 MB)
"""

"""
快慢指針
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
"""
Accepted
113/113 cases passed (39 ms)
Your runtime beats 95.96 % of python3 submissions
Your memory usage beats 38.51 % of python3 submissions (16.5 MB)
"""
# @lc code=end


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))
