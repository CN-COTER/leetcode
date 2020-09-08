#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = OrderedDict()


    def get(self, key: int) -> int:
        value = self.queue.get(key, -1)
        if key in self.queue:
            self.queue.move_to_end(key, last=True)
        return value



    def put(self, key: int, value: int) -> None:
        self.queue[key] = value
        self.queue.move_to_end(key, last=True)
        if len(self.queue) > self.capacity:
            self.queue.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

