# 給予一整數x，如果x為回文則回傳true
# For example, 121 is a palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads - 121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Solution：
################################
# class Solution:
#     def isPalindrome(self, x):
#         str_x = str(x)
#         buffer = []
#         for i in str_x:
#             buffer.append(i)
#         if buffer[::-1] == buffer:
#             return True
################################

# Chllange solution : solve it without convert int to string

################################
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """

    # r:最小位數
    r = 0

    # m:最大位數
    m = x

    # 如果x是負數則不可能為回文
    if x < 0:
        return False

    while x > 0:
        # r*10：從最小位數開始一位一位往前推
        # x%10：取目前最大位數的數字
        r = r*10 + x % 10
        # 把x的值往前推(//代表整除的意思)
        x = x // 10
    return r == m
################################

# example : 12321

# r 0+1=1
# x 1232

# r 10+2=12
# x 123

# r 120+3=123
# x 12

# r 1230+2=1232
# x 1

# r 12320+1
# x 0

# x 不再>0 跳脫while迴圈

# r == m 回傳true
