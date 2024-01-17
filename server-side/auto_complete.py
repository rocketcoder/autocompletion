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

trie.insertString("hattle")
trie.insertString("hang")
trie.insertString("hoat")
trie.insertString("hottle")
trie.insertString("hank")
trie.insertString("hlitz")
trie.insertString("hlix")
trie.insertString("hait")



trie.insertString("hry")
trie.insertString("hrate")
trie.insertString("hate")
trie.insertString("all")
trie.insertString("air")
trie.insertString("ally")
trie.insertString("ats")
trie.insertString("apple")



trie.insertString("hi")
trie.insertString("hey")
trie.insertString("height")
trie.insertString("hike")
trie.insertString("hick")
trie.insertString("hickey")
trie.insertString("hint")
trie.insertString("hit")



trie.insertString("appolo")
trie.insertString("high")
trie.insertString("heat")
trie.insertString("heater")
trie.insertString("heath")
trie.insertString("ates")
trie.insertString("apply")
trie.insertString("application")
 
def complete(msg):
    return trie.findCompletions(msg)