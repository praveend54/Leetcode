# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l.sort()
        res=ListNode(0)
        dummy=res
        for i in l:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return res.next