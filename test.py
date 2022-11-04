from copy import deepcopy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

b = ListNode()
a =  deepcopy(b)

print(a is b)