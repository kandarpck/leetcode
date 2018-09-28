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
    def isPalindrome(self, head):
        """
        Time: N
        Space: 1
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        rev = None
        # find the midpoint of the LL
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # if odd number of elements in the LL
        if fast:
            slow = slow.next

        # compare reversed first half to second
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().isPalindrome(head))
