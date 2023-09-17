#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start


# two queue
# class MyStack:
#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []
#         self.active_queue = self.queue1

#     def push(self, x: int) -> None:
#         self.active_queue.append(x)

#     def pop(self) -> int:
#         inactive_queue = self.queue2 if self.active_queue == self.queue1 else self.queue1
#         while len(self.active_queue) > 1:
#             inactive_queue.append(self.active_queue.pop(0))
#         ret_value = self.active_queue.pop(0)
#         self.active_queue, inactive_queue = inactive_queue, self.active_queue
#         return ret_value
        
#     def top(self) -> int:
#         inactive_queue = self.queue2 if self.active_queue == self.queue1 else self.queue1
#         while len(self.active_queue) > 1:
#             inactive_queue.append(self.active_queue.pop(0))
#         ret_value = self.active_queue[0]
#         inactive_queue.append(self.active_queue.pop(0))
#         self.active_queue, inactive_queue = inactive_queue, self.active_queue
#         return ret_value

#     def empty(self) -> bool:
#         return len(self.active_queue) == 0
    
    
# one queue
class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
    
    def top(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        temp = self.queue.pop(0)
        self.queue.append(temp)
        return temp

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
