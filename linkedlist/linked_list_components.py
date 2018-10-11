class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def numOfComponents(self, head, G):
        """
        :param head:
        :param G:
        :return: int
        Time: N
        Space: N
        """
        lookup = set(G)
        curr = ListNode(-1)
        curr.next = head
        res = 0
        while curr and curr.next:
            if curr.val in lookup and curr.next.val not in lookup:
                res += 1
            curr = curr.next
        return res


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    G = [0, 3, 1, 4]
    print(Solution().numOfComponents(head, G))

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    G = [1, 2, 4]
    print(Solution().numOfComponents(head2, G))
