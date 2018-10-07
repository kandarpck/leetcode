# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        Time: O(n + m)
        Space: 1
        """
        if not (headA and headB):
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


if __name__ == "__main__":
    head3 = ListNode(4)
    head3.next = ListNode(5)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next = head3

    head2 = ListNode(11)
    head2.next = ListNode(22)
    head2.next.next = ListNode(33)
    head2.next.next.next = head3

    print(Solution().getIntersectionNode(head, head2))

    head4 = ListNode(1)
    head4.next = ListNode(2)
    head4.next.next = ListNode(3)

    head5 = ListNode(11)

    print(Solution().getIntersectionNode(head4, head5))
