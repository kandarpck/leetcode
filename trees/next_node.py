# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    # @param root, a tree link node
    # @return nothing
    # Time: N
    # Space: h
    def connect(self, root):
        if not root:
            return None
        current = [root]
        while current:
            next_level = []
            for idx in range(len(current)):
                node = current[idx]
                next_node = current[idx + 1] if idx + 1 < len(current) else None
                if not node:
                    continue
                else:
                    node.next = next_node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    Solution().connect(root)
    print(root, root.next, root.left, root.left.next, root.left.next.next)
