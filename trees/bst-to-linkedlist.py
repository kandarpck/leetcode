class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        if not self:
            return 'nil'
        return '{} -> {}'.format(self.value, repr(self.next))


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        if not self:
            return 'nil'
        return '{}'.format(self.value)


class Solution(object):
    def convert_bst_to_linked_list(self, root):
        dummy = order = LinkedListNode('-inf')
        self.inorder_traversal(order, root)
        return dummy

    def inorder_traversal(self, order, root):
        if root is None:
            return
        self.inorder_traversal(order, root.left)
        order.next = LinkedListNode(root.value)
        order = order.next
        self.inorder_traversal(order, root.right)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    print(Solution().convert_bst_to_linked_list(root))
