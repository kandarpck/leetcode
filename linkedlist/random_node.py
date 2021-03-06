from random import randint


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
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        """
        :param head:
        :param G:
        :return: int
        Time: N
        Space: N
        """
        reservoir = -1
        curr, n = self.head, 0
        while curr:
            reservoir = curr.val if randint(1, n + 1) == 1 else reservoir
            curr = curr.next
            n += 1
        return reservoir


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution(head).getRandom())
