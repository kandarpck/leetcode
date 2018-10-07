# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Time: N
        Space: N
        """
        order = []
        self.postorderTraversalRecursive(order, root)
        return order

    def postorderTraversalRecursive(self, order, root):
        if not root:
            return
        self.postorderTraversalRecursive(order, root.left)
        self.postorderTraversalRecursive(order, root.right)
        order.append(root.val)


class Solution2(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Time: N
        Space: h
        """
        result, stack = [], [(root, False)]
        while stack:
            node, is_visited = stack.pop()
            if not node:
                continue
            if is_visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().postorderTraversal(root))

    print(Solution2().postorderTraversal(root))
