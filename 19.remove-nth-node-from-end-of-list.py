#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time complexity = O(N*n)
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = head
        prev = dummy

        if head.next == None:
            return None

        while curr:

            # 檢測curr是否為倒數第n個項目 None的話就是
            temp = curr
            for _ in range(n):
                temp = temp.next

            # 要刪除curr
            if temp == None:
                # 處理刪除head的方法
                if curr == head:
                    return head.next

                # 處理普通刪除情況
                curr = curr.next
                prev.next = curr
                return head

            # 不用刪除curr
            else:
                prev = curr
                curr = curr.next
        return head


# time complexity = O(N)
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next
        # if fast == None:
        #     return head.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        # return head
        return dummy.next


# @lc code=end
