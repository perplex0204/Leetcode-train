#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    # 暴力解
    # str.replace(old, new[, max])
    # old -- 将被替换的子字符串。
    # new -- 新字符串，用于替换old子字符串。
    # max -- 可选字符串, 替换不超过 max 次
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in list(magazine):
            if letter in list(ransomNote):
                ransomNote = ransomNote.replace(letter, '', 1)
        if ransomNote == '':
            return True
        else:
            return False

    # 使用dict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        hashmap = {}
        for letter in list(magazine):
            hashmap[letter] = hashmap.get(letter, 0) + 1
        for letter in list(ransomNote):
            if hashmap.get(letter, 0) == 0:
                return False
            else:
                hashmap[letter] -= 1
        return True

    # 使用Counter相減
    # print(Counter('aabbcc'))                                              # Counter({'a': 2, 'b': 2, 'c': 2})
    # print(Counter('aaaaabbcc'))                                           # Counter({'a': 5, 'b': 2, 'c': 2})
    # print(Counter('aabahaehagagagrargbcc') - Counter('aaaaabbcc'))        # Counter({'g': 4, 'a': 3, 'h': 2, 'r': 2, 'e': 1})
    # print(Counter('aaaaabbcc') - Counter('aabahaehagagagrargbcc'))        # Counter()
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        return not Counter(ransomNote) - Counter(magazine)

    # 使用all
    # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True

        # 一行流
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))
# @lc code=end
