#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def happy_cal(self, n: int) -> int:
        result = 0
        for num in list(str(n)):
            result = result + int(num) * int(num)
        return result

    # 第一個想法：
    # Your runtime beats 72.63 % of python3 submissions
    # Your memory usage beats 68.08 % of python3 submissions (16.2 MB)
    def isHappy(self, n: int) -> bool:
        while n != 1:
            n = self.happy_cal(n)
            if n == 4:
                return False
        return True

    # hash
    # Your runtime beats 92.1 % of python3 submissions
    # Your memory usage beats 32.34 % of python3 submissions (16.3 MB)
    def isHappy(self, n: int) -> bool:
        hash_map = set()
        while n != 1:
            n = self.happy_cal(n)
            if n in hash_map:
                return False
            hash_map.add(n)
        return True
# @lc code=end
