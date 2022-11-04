from collections import deque
from copy import deepcopy


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
        
        dummy = current = ListNode()

        while True:
            if list1 == None:
                # print("list1 none")
                current.next = list2
                break
            if list2 == None:
                # print("list2 none")
                current.next = list1
                break

            if list1.val < list2.val:
                # print("bigger")
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                # print("smaller")
                current.next = list2
                list2 = list2.next
                current = current.next
            
        return dummy.next

def list_2_listNode(l):
    dummy = prev = ListNode()
    
    for e in l:
        node = ListNode(val=e)
        prev.next = node
        prev = prev.next
    
    return dummy.next

def printListNode(node: ListNode):
    while node != None:
        print(node.val, end=" ")
        node = node.next



        


S = Solution()
# test1 = [1,2,3]
# test2 = [1,4,5]
test1 = []
test2 = [1,2,3]
node1 = list_2_listNode(test1)
node2 = list_2_listNode(test2)
# printListNode(node)
result = S.mergeTwoLists(node1, node2)
printListNode(result)