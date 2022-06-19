# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Solution:
################################
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        # 空陣列的情況
        if not strs:
            return ""

        #i = index
        # letter_group = strs的數組，這樣用的好處是
        # 1. letter_group數量 = 最短的那個單字的長度
        # 2. 可以使用set(letter_group)來直接檢查是否有重複
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                # 回傳第0個數據的0~i個資料
                return strs[0][:i]
        else:
            return min(strs)
################################

# 嘗試的程式
# 思路：先找出最短的單字，將其拆成一個字一個元素的list
# 再用最短的長度寫第一層for enumerate 有最短單字的index(第幾個字)跟單字(單一英文)
# 再寫第二層for，去比較所有元素的第幾個index是否相同，相同則丟進buffer，最後再把相同的元素去掉，剩下解答

# 問題：找出最短的單字是有成功的
# 但是雙層for在比較的時候會造成重複輸入答案list，最後會有非完整相同的元素會多出來，造成repeat_check()無法正常工作
################################
# def repeat_check(input):
#     check_done = []
#     for data in input:
#         #初始化
#         if check_done == []:
#             check_done.append(data)

#         for check in check_done:
#             check_flag = False
#             if data == check:
#                 check_flag = False
#             else:
#                 check_flag = True
#         if check_flag == True:
#             check_done.append(data)
#     return check_done
# class Solution:
#     def longestCommonPrefix(self, strs):
#         answer = ''
#         buffer1 = []
#         buffer2 = []
#         shortest = 0
#         for index, data in enumerate(strs):
#             if index == 0:
#                 shortest = len(data)
#                 shortest_index = 0
#             if len(data) < shortest:
#                 shortest = len(data)
#                 shortest_data = data
#                 shortest_index = index


#         # 取最短的單字，一個一個比
#         for index, i in enumerate(strs[shortest_index]):
#             buffer1.append(shortest_data[index])
#             for data in strs:
#                 if not data[index] == shortest_data[index]:
#                     break
#                 else:
#                     buffer2.append(buffer1[index])
#         print(buffer2)
#         answer_list = repeat_check(buffer2)
#         for data in answer_list:
#             answer += data
#         print(answer)
################################

# 學習到的新知

lst = ['1asdfasfd', '2asdfsadf', '3awegwgewe']
rep = ['4' if x == '2' else x for x in lst]


# 查阅资料后发现，参数前面加上*号
# 意味着参数的个数不止一个
# 另外带一个星号（*）参数的函数传入的参数存储为一个元组（tuple）
# 带两个（*）号则是表示字典（dict）
for index, data in enumerate(zip(*lst)):
    print(data)
# 資料型態：tuple
# ('1', '2', '3')
# ('a', 'a', 'a')
# ('s', 's', 'w')
# ('d', 'd', 'e')
# ('f', 'f', 'g')
# ('a', 's', 'w')
# ('s', 'a', 'g')
# ('f', 'd', 'e')
# ('d', 'f', 'w')

# 集合 set()
# https://wenyuangg.github.io/posts/python3/python-set.html
# 集合 (Set) 其實和數組 (Tuple) 與串列 (List) 很類似, 不同的點在於集合不會包含重複的資料
