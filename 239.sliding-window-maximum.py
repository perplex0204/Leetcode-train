#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (46.13%)
# Likes:    17037
# Dislikes: 582
# Total Accepted:    888.4K
# Total Submissions: 1.9M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from typing import List
# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        result = []
        for i in range(k):
            queue.append(nums[i])
        result.append(max(queue))
        for i in range(len(nums) - k):
            queue.pop(0)
            queue.append(nums[i+k])
            result.append(max(queue))
        return result

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        # 初始化隊列和結果列表
        queue = []
        result = []

        # 進行遍歷
        for i, n in enumerate(nums):
            print(queue)
            # 移除超出窗口範圍的索引（模仿 popleft 操作）
            while queue and queue[0] < i - k + 1:
                queue.pop(0)

            # 從隊列尾部開始，刪除所有小於當前元素的數字，以保持隊列的有序性（最大的數在前面）
            while queue and nums[queue[-1]] < n:
                queue.pop()

            queue.append(i)

            # 窗口形成後，開始添加結果
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
# @lc code=end


s = Solution
print(s.maxSlidingWindow(self=s, nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
