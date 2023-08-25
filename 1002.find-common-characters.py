#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (68.51%)
# Likes:    3254
# Dislikes: 256
# Total Accepted:    188.5K
# Total Submissions: 275.1K
# Testcase Example:  '["bella","label","roller"]'
#
# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the
# answer in any order.
#
#
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
#
#

from typing import List

# @lc code=start


class Solution:
    # 第一個想法
    def commonChars(self, words: List[str]) -> List[str]:
        hash_table = {}
        result = []
        for word in words:
            for letter in word:
                if letter in hash_table:
                    hash_table[letter] += 1
                else:
                    hash_table[letter] = 1
        for key, value in hash_table.items():
            if value >= len(words):
                for _ in range(value // len(words)):
                    result.append(key)
        return result

    # 第二個想法
    # time: O(N*M)
    # space: O(N*M)
    def commonChars(self, words: List[str]) -> List[str]:
        hash_table = {}
        result = []
        for word_index, word in enumerate(words):
            for letter in word:
                if letter not in hash_table:
                    hash_table[letter] = [0]*len(words)
                hash_table[letter][word_index] += 1
        for letter in hash_table:
            if min(hash_table[letter]) != 0:
                for _ in range(min(hash_table[letter])):
                    result.append(letter)
        return result

    # python sol
    # time: O(N*M)
    # space: O(1)
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        res = Counter(words[0])
        # Counter({'d': 3, 'a': 2, 'c': 2, 'b': 1})
        print(res)
        for i in words:
            res &= Counter(i)
        return list(res.elements())

    # 代碼隨想錄 1
    # time: O(N*M)
    # space: O(1)
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        result = []
        hash = [0] * 26  # 用来统计所有字符串里字符出现的最小频率
        for i, c in enumerate(words[0]):  # 用第一个字符串给hash初始化
            hash[ord(c) - ord('a')] += 1
        # 统计除第一个字符串外字符的出现频率
        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in range(len(words[i])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1
            # 更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])
        # 将hash统计的字符次数，转成输出形式
        for i in range(26):
            while hash[i] != 0:  # 注意这里是while，多个重复的字符
                result.extend(chr(i + ord('a')))
                hash[i] -= 1
        return result

    # 代碼隨想錄 2
    # time: O(N*M)
    # space: O(1)

    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        tmp = Counter(words[0])
        l = []
        for i in range(1, len(words)):
            # 使用 & 取交集
            tmp = tmp & Counter(words[i])

        # 剩下的就是每个单词都出现的字符（键），个数（值）
        for j in tmp:
            v = tmp[j]
            while (v):
                l.append(j)
                v -= 1
        return l
# @lc code=end


print(Solution().commonChars(["acabcddd", "bcbdbcbd", "baddbadb",
      "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]))
print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["cool", "lock", "cook"]))
