class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        return currentNode.endOfString

    def findCompletions(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        return self._findWordsFromNode(node, prefix)

    def _findWordsFromNode(self, node, prefix):
        words = []
        if node.endOfString:
            words.append(prefix)

        for char, next_node in node.children.items():
            words.extend(self._findWordsFromNode(next_node, prefix + char))

        return words

# Example Usage
trie = Trie()
trie.insertString("hello")
trie.insertString("helium")
trie.insertString("help")
trie.insertString("helicopter")
trie.insertString("health")
trie.insertString("hat")
trie.insertString("at")
trie.insertString("ate")
 
def complete(msg):
    return trie.findCompletions(msg)