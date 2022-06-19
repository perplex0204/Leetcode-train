# Given an array of integers nums and an integer target
# , return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution
# , and you may not use the same element twice.
# You can return the answer in any order.

# Solution:
################################
class Solution:
    def twoSum(self, nums, target):
        # enumerate()：回傳index與資料
        for index, data in enumerate(nums):
            # 判斷資料是否可能有解
            if target - data in nums:
                # 判斷資料是否重複
                # list.index(data)：回傳該data的index，要確定該資料在list內，否則Value Error
                # 如果有相同的情況會先回傳比較小的index
                # 因為答案只會有一個組合所以才可以這樣寫
                if nums.index(target - data) != index:
                    return(index, nums.index(target - data))
# 因為答案只會有一個所以才可以這樣寫
################################

# example nums：
# [3,3,2,5]

# example target：
# 6
