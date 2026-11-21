# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        curr = head
        N = 0
        while curr:
            N+=1
            curr = curr.next
        
        target = N-n

        if target == 0:
            return head.next
        curr = head
        i=1
        while curr:

            if i==target:
                curr.next = curr.next.next
                return head
            curr=curr.next
            i+=1
        
        

