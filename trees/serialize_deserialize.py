# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def serializeHelper(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            serializeHelper(node.left)
            serializeHelper(node.right)

        vals = []
        serializeHelper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        def deserializeHelper():
            elem = next(vals)
            if elem == '#':
                return None
            node = TreeNode(int(elem))
            node.left = deserializeHelper()
            node.right = deserializeHelper()
            return node

        vals = iter(data.split())
        return deserializeHelper()


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    codec = Codec()
    r2 = codec.deserialize(codec.serialize(root))
    print(r2.val, r2.left, r2.right, r2.left.left)
