# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in [None, p, q]:
            return root

        left, right = [self.lowestCommonAncestor(child, p, q) for child in [root.left, root.right]]

        return root if left and right else left or right


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().lowestCommonAncestor(root, root.right, root.right.right))
