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
    def connect(self, root):
        current = [root]
        while current:
            next_level = []
            for idx in range(len(current)):
                node = current[idx]
                next_node = current[idx + 1] if idx + 1 < len(current) else None
                if not node:
                    return None
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
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    Solution().connect(root)
    print(root, root.next, root.left, root.left.next, root.left.next.next, root.left.left, root.left.left.next, root.left.left.next.next)
