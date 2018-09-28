# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution(object):
    # @param root, a tree node
    # @return a boolean
    # Time: N
    # Space: N
    def isValidBST(self, root):
        output = []
        self.inOrderTraversal(root, output)
        for i in range(1, len(output)):
            if output[i - 1].val >= output[i].val:
                return False
        return True

    def inOrderTraversal(self, root, output):
        if root is None:
            return
        self.inOrderTraversal(root.left, output)
        output.append(root)
        self.inOrderTraversal(root.right, output)


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(Solution().isValidBST(root))
