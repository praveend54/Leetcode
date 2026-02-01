# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=""
        b=""
        while l1:
            a+=str(l1.val)
            l1=l1.next
        while l2:
            b+=str(l2.val)
            l2=l2.next
        res=int(a[::-1])+int(b[::-1])
        if res==0:
            return ListNode(0)
        head=ListNode(0)
        dummy=head
        while res>0:
           dummy.next=ListNode(res%10)
           dummy=dummy.next
           res//=10
        return head.next