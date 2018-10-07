# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Time: N
        Space: N
        """
        order = []
        self.preorderTraversalRecursive(order, root)
        return order

    def preorderTraversalRecursive(self, order, root):
        if not root:
            return
        order.append(root.val)
        self.preorderTraversalRecursive(order, root.left)
        self.preorderTraversalRecursive(order, root.right)


class Solution2(object):

    def preorderTraversal(self, root):
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
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().preorderTraversal(root))

    print(Solution2().preorderTraversal(root))
