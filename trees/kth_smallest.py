# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        Time: N
        Space: h
        """
        output = []
        self.inorder(output, root)
        return output[k - 1]

    def inorder(self, output, root):
        if not root:
            return None
        self.inorder(output, root.left)
        output.append(root.val)
        self.inorder(output, root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(Solution().kthSmallest(root, k=3))
