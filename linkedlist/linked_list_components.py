class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def numOfComponents(self, head, G):
        """
        :param head:
        :param G:
        :return:
        """
        pass


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    G = [0, 3, 1, 4]

    print(Solution().numOfComponents(head, G))
