# Time:  O(1)
# Space: O(1)
#
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
# with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
#
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
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, head, v):
        curr = dummy = ListNode(-1)
        dummy.next = head
        while dummy and dummy.next:
            if dummy.next.val == v:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return curr.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(Solution().deleteNode(head, 1))
