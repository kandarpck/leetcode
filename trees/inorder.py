# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

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


class Solution2(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().inorderTraversal(root))
