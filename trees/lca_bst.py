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
        r, s = sorted([p.val, q.val])

        while not r <= root.val <= s:
            root = root.left if r <= root.val else root.right

        return root


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().lowestCommonAncestor(root, root.left, root.right))
