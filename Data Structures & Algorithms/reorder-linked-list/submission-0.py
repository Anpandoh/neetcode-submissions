# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle using fast slow pointer
        slow , fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print(slow.val)

        #slow is now midpoint
        #reverse from middle
        second = slow.next
        prev = slow.next = None #need to set slow.next to break apart the 2 lists
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # prev = None
        # slow = slow.next
        # while slow:
        #     temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = temp

        # while prev:
        #     print(prev.val)
        #     prev = prev.next

        #go down from both sides till you reach the middle
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        # start = head
        # second = prev
        # while second:
        #     tempO = start.next
        #     tempA = second.next
        #     start.next = second
        #     second.next = tempO
        #     start = tempO
        #     second = tempA

