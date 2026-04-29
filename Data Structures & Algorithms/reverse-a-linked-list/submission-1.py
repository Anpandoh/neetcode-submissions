# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#sN = B -> C
#sN = C

#A -> B ->  C
#A -> B -> A
# B -> C -> B
# B -> C


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currNode = head
        prevNode = None
        while currNode:
            nextTemp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextTemp
        
        return prevNode






        