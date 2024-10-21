# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result_head = result = ListNode()

        head1 = list1
        head2 = list2

        while (head1 or head2):
            if (head1 and head2):
                if head1.val < head2.val:
                    result.next = ListNode(head1.val)
                    result = result.next
                    head1 = head1.next
                else:
                    result.next = ListNode(head2.val)
                    result = result.next
                    head2 = head2.next

            elif not head1:
                result.next = ListNode(head2.val)
                result = result.next
                head2 = head2.next
            
            elif not head2:
                result.next = ListNode(head1.val)
                result = result.next
                head1 = head1.next

        return result_head.next