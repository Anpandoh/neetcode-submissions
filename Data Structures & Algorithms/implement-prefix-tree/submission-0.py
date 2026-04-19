class TreeNode:
    def __init__(self):
        self.children = {} #dict which can contain any of the 26 possible letters in the alphabet for each level
        self.isEnd = False
    
class PrefixTree:


    def __init__(self):
        self.startNode = TreeNode()
        

    def insert(self, word: str) -> None:
        currNode = self.startNode
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TreeNode()
            currNode = currNode.children[char]
        currNode.isEnd = True
            
            



    def search(self, word: str) -> bool:
        currNode = self.startNode
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.isEnd

        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.startNode
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True

        
        