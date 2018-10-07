# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


if __name__ == "__main__":
    preorder = [1, 2, 3, 4]
    inorder = [2, 1, 3, 4]
    root = Solution().buildTree(preorder, inorder)
    print(root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right)
