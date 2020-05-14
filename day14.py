'''
Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

'''
class trieNode:
    def __init__(self):
        self.isWord = False
        self.child = [None] * 26
class Trie:
    def __init__(self):
        self.root = trieNode()
    def insert(self,word):
        current = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if current.child[index] == None:
                current.child[index] = trieNode()
            current = current.child[index]
        current.isWord = True
    def search(self,word):
        current = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if current.child[index] == None:
                return False
            current = current.child[index]
        return current.isWord == True
    def startsWith(self,prefix):
        current = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if current.child[index] == None:
                return False
            current = current.child[index]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
