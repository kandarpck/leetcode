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
    def reverseList(self, head):
        """
        Time: N
        Space: 1
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = None
        while head:
            curr = head
            head = head.next
            curr.next = dummy
            dummy = curr

        return dummy

    def reverseListRecursive(self, head):
        """
        Time: N
        Space: N
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().reverseListRecursive(head))
