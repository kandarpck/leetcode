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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = new_node = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            new_node.next = ListNode((a + b + carry) % 10)
            carry = (a + b + carry) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            new_node = new_node.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)

    head2 = ListNode(9)
    head2.next = ListNode(9)

    print(Solution().addTwoNumbers(head, head2))
   