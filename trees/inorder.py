def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    order = []
    self.inorderTraversalRecursive(order, root)
    return order


def inorderTraversalRecursive(self, order, root):
    if not root:
        return
    self.inorderTraversalRecursive(order, root.left)
    order.append(root.val)
    self.inorderTraversalRecursive(order, root.right)
