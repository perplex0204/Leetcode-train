#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
# @lc code=start
#时间复杂度：O(nlogk)
#空间复杂度：O(n)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for num in nums:
            map_[num] = map_.get(num, 0) + 1

        # sorted(iterable, cmp=None, key=None, reverse=False)
        sorted_items = sorted(map_.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result
# @lc code=end

s = Solution
print(s.topKFrequent(self=s, nums= [1,1,1,2,2,3,3,3,3,33,3,3,2,123,14,1,4,45,2345,235,1231,11,34,1243,1243,3,412,3412,4312,34512,3424,33,33,33,33,33,33], k = 2))