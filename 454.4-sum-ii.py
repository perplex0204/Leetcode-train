#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import List
# @lc code=start


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1

        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - (n3 + n4)
                if key in hashmap:
                    count += hashmap[key]
        return count

    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                # dict.get(key, value): 如果key不存在，返回value
                # 省略if-else
                hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1

        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - (n3 + n4)
                if key in hashmap:
                    count += hashmap[key]
        return count

    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        from collections import defaultdict
        # 它會自動為不存在的鍵分配初始值0。這樣可以減少檢查鍵是否存在的需求。
        hashmap = defaultdict(lambda: 0)
        for n1 in nums1:
            for n2 in nums2:
                # 再更省略.get()
                hashmap[n1+n2] += 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                count += hashmap.get(-(n3+n4), 0)
        return count
# @lc code=end
