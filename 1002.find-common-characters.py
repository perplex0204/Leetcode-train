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
# @lc code=end


print(Solution().commonChars(["acabcddd", "bcbdbcbd", "baddbadb",
                              "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]))
