'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

'''
#以為是list的程式
list1 = [1, 2, 4]
list2 = [1, 3, 4]
answer = []
list1.extend(list2)

for i in range(len(list1)):
    answer.append(min(list1))
    list1.remove(min(list1))
print(answer)
'''

'''
問題：
搞清楚class的用法與listnode的val、next是什麼意思
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode()
list2 = ListNode([1, 3, 4])

print(list1.val)

print(list1.next)
