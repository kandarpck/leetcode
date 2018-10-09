# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left, root.right = self.trimBST(root.left, L, R), self.trimBST(root.right, L, R)
        return root


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right = TreeNode(4)

    r2 = Solution().trimBST(root, 1, 3)
    print(r2.val, r2.left, r2.left.left, r2.right)
