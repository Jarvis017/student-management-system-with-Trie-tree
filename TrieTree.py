class Node:
    def __init__(self):

        # initialize node
        self.key = None
        self.children = [None] * 10

    # find key from prefix
    def findChildren(self, node, arr):
        if node.key is not None:
            return arr.append(node.key)
        for i in range(len(node.children)):
            if node.children[i] is not None:
                node.findChildren(node.children[i], arr)
        return arr


class TrieTree:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return Node()

    # insertion in tree
    def insert(self, num, key):
        num = str(num)
        CurrentNode = self.root

        # find last  character of number
        for i in range(len(num)):
            index = int(num[i])
            if not CurrentNode.children[index]:
                CurrentNode.children[index] = self.getNode()
            CurrentNode = CurrentNode.children[index]

        # put hash key in last character
        CurrentNode.key = key

    def search(self, num):
        num = str(num)
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        CurrentNode = self.root
        for i in range(len(num)):
            index = int(num[i])
            if not CurrentNode.children[index]:
                return False
            CurrentNode = CurrentNode.children[index]

        return CurrentNode is not None and CurrentNode.key is not None

    # get hash key from hash table
    def GetKey(self, num):
        num = str(num)
        CurrentNode = self.root

        # find last node
        for i in range(len(num)):
            index = int(num[i])
            CurrentNode = CurrentNode.children[index]
        return CurrentNode.key

    def isEmpty(self, node):
        for i in range(11):
            if node.children[i] is not None:
                return False
        return True

    # deletion method
    def Delete(self, num):
        num = str(num)
        CurrentNode = self.root

        # find last character
        for i in range(len(num)):
            index = int(num[i])
            CurrentNode = CurrentNode.children[index]

        # set None for node's key
        CurrentNode.key = None

    # suggestion method
    def preSearch(self, num):
        num = str(num)
        CurrentNode = self.root

        # find last character node
        for i in range(len(num)):
            index = int(num[i])
            CurrentNode = CurrentNode.children[index]
        tmp = []
        if CurrentNode is None:
            return

        # search in children's node for hash key
        keys = CurrentNode.findChildren(CurrentNode, tmp)
        if keys is None:
            keys = []

        # search for full number in tree ( handle the bug )
        if self.search(num):
            keys.append(self.GetKey(num))
        return list(keys)
