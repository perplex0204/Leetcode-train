# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.md
#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0               # 起始点
        loop = n // 2                       # 每个圈循环几次，例如n为奇数3，那么loop = 1 只是循环一圈，矩阵中间的值需要单独处理
        # 矩阵中间的位置，例如：n为3， 中间的位置就是(1，1)，n为5，中间位置为(2, 2)
        mid = n // 2
        count = 1                           # 要填入的數字

        # 一個offset就是模擬轉了一圈的情況，每次循環結束offset + 1，代表內縮一格
        for offset in range(1, loop + 1):           # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset):     # 从左至右
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):     # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1

            startx += 1
            starty += 1
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

# @lc code=end


sol = Solution()
print(sol.generateMatrix(5))
