from queue import *

class binaryTree:
    def __init__(self, value):
        self.data = value
        self.count = 1 #used to manage the duplicate values
        self.left = None
        self.right = None
        self.queue = Queue()

    def insert(self, value):
        if value == self.data:
            self.count = self.count + 1
        elif value > self.data:
            if not self.left:
                self.left = binaryTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = binaryTree(value)
            else:
                self.right.insert(value)

    def printTree(self, level=0):
        #this printing function is using DFS algorithm
        print('data -> {}, count => {}, level [{}]'.format(self.data, self.count, level))
        try:
            self.left.printTree(level+1)
        except:
            pass
        try:
            self.right.printTree(level+1)
        except:
            pass
    
    def printTreeUsingBFS(self):
        self.queue.push(self)
        self.bfsTraverse()
        return

    def bfsTraverse(self):
        value = self.queue.pop()
        if value == None:
            return
        else:
            print(value.data)
            if value.left != None:
                self.queue.push(value.left)
            if value.right != None:
                self.queue.push(value.right)
            self.bfsTraverse()


binTree = binaryTree(150)
binTree.insert(210)
binTree.insert(110)
binTree.insert(160)
binTree.insert(150)
binTree.insert(250)
binTree.insert(1)
binTree.insert(2)

binTree.printTreeUsingBFS()
binTree.printTree()