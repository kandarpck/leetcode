class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if char not in curr.leaves:
                curr.leaves[char] = TrieNode()
            curr = curr.leaves[char]
        curr.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.childSearch(word)
        return node.is_string if node else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.childSearch(prefix) is not None

    def childSearch(self, word):
        curr = self.root
        for char in word:
            if char in curr.leaves:
                curr = curr.leaves[char]
            else:
                return None
        return curr


if __name__ == '__main__':
    word = "apple"
    prefix = "app"
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
    print(param_2, param_3, obj.search('kandarp'))
