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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Time: N
        Space: 1
        """
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            even_head = slow.next
            slow.next = fast.next
            slow = slow.next
            fast.next = slow.next
            slow.next = even_head
            fast = fast.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().oddEvenList(head))
