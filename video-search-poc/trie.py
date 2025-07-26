# trie.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect(node, prefix)

    def _collect(self, node, prefix):
        words = []
        if node.is_end:
            words.append(prefix)
        for char, nxt in node.children.items():
            words.extend(self._collect(nxt, prefix + char))
        return words
