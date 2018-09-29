# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution(object):
    def isSymmetric(self, root):
        """
        Time: N
        Space: h
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = list()
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            p, q = stack.pop(), stack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)
        return True

    def isSymmetricRecursive(self, root):
        """
        Time: N
        Space: h
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isSymmetricRecur(root.left, root.right)

    def isSymmetricRecur(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False

        return self.isSymmetricRecur(left.left, right.right) and self.isSymmetricRecur(left.right, right.left)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    print(Solution().isSymmetricRecursive(root))

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(4)
    print(Solution().isSymmetricRecursive(root2))
