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
        ListNode dummy1 = new ListNode(0);
        dummy1.next=head;
        ListNode first = dummy1;
        ListNode second = dummy1;

        int counter =0;

        while (counter < n){
            second=second.next;
            counter++;
        }

        while (second.next != null){
            second = second.next;
            first = first.next;
        }

        first.next = first.next.next;





        return dummy1.next;
    }
}
