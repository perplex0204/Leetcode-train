#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.14%)
# Likes:    10240
# Dislikes: 322
# Total Accepted:    2.5M
# Total Submissions: 4M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start
class Solution:

    # 第一個想法
    # time: O(N^2)
    # space: O(N)
    # Your runtime beats 5.03 % of python3 submissions
    # Your memory usage beats 23.58 % of python3 submissions (17.4 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        list_s = list(s)
        list_t = list(t)
        
        for letter in list_s:
            if letter not in list_t:
                list_t.remove(letter)
            else:
                return False
        return True

    # 改善原想法
    # time: O(N^2)
    # space: O(1)
    # Your runtime beats 5.65 % of python3 submissions
    # Your memory usage beats 87 % of python3 submissions (16.7 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in t:
                t = t.replace(letter, '', 1)
            else:
                return False
        return True

    # time: O(N)
    # space: O(N)
    # 42/42 cases passed (42 ms)
    # Your runtime beats 97.73 % of python3 submissions
    # Your memory usage beats 61.62 % of python3 submissions (16.9 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

    # time: O(N)
    # space: O(N)
    # Your runtime beats 48.58 % of python3 submissions
    # Your memory usage beats 36.49 % of python3 submissions (16.9 MB)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = {}
        for letter in s:
            if letter in hash_table:
                hash_table[letter] += 1
            else:
                hash_table[letter] = 1
        for letter in t:
            if letter in hash_table:
                hash_table[letter] -= 1
                if hash_table[letter] == 0:
                    del hash_table[letter]
            else:
                return False
        return True

# @lc code=end
