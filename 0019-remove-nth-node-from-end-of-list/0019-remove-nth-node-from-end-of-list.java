/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode x=head;
        int c=0;
        while(x!=null){
            c++;
            x=x.next;
        }
        int y=c-n-1;
        ListNode a=head;
        while(a!=null && y!=0){
            a=a.next;
            y-=1;
        }
        if(a==null){
            return head.next;
        }
        a.next=a.next.next;
        return head;
    }
}