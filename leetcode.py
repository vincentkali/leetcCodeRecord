from collections import deque
from copy import deepcopy
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list2.val > list1.val:
            header = deepcopy(list2)
            current = deepcopy(list2)
            prev = deepcopy(list2)
        else:
            header = deepcopy(list1)
            current = deepcopy(list1)
            prev = deepcopy(list1)
        
        while True:
            if 


S = Solution()
test = ']'
result = S.isValid(test)
print(result)