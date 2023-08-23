#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class MyLinkedList:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        self.head = MyLinkedList(val=val, next=self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = MyLinkedList(val=val)
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = MyLinkedList(val=val)
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return None
        curr = self.head
        prev = None
        for _ in range(index):
            if not curr:
                return
            prev = curr
            curr = curr.next
        prev.next = MyLinkedList(val=val, next=curr)
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return None
        curr = self.head
        prev = None
        for _ in range(index):
            if not curr:
                return
            prev = curr
            curr = curr.next
        if prev and curr:
            prev.next = curr.next
        return None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
