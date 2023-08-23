#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# time complexity = O(N^2)
# 因為if x in list要遍歷整個list
# Error - Found cycle in the ListNode
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = []
        while curr:
            if curr in temp:
                return curr
            else:
                temp.append(curr)
                curr = curr.next
        return None


# # 快慢指針
# time complexity = O(N)
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None


# set
# time complexity = O(N)
# 因為 set 查找 時間複雜度為O(1)
class Solution3:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None
# @lc code=end
