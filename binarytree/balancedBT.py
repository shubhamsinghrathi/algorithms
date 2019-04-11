class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.head = None

    def balancer(self, node, level=0):
        left = level
        right = level
        if node.left:
            left = self.balancer(node.left, level+1)
        if node.right:
            right = self.balancer(node.right, level+1)
        node.balance = left-right
        if left>right:
            return left
        else:
            return right

    def LLRotation(self, node):
        mainNode = node.left
        node.left = mainNode.right
        mainNode.right = node
        return mainNode
        

    def RRRotation(self, node):
        mainNode = node.right
        node.right = mainNode.left
        mainNode.left = node
        return mainNode

    def LRRotation(self, node):
        self.treePrinter(node.left)
        node.left = self.RRRotation(node.left)
        self.treePrinter(node.left)
        return self.LLRotation(node)
    
    def RLRotation(self, node):
        node.right = self.LLRotation(node.right)
        return self.RRRotation(node)

    def inserter(self, node, data):
        direction = ""
        res = {}
        if node.data > data and node.left != None:
            direction = "L"
            res = self.inserter(node.left, data)
        elif node.data > data and node.left == None:
            node.left = Node(data)
            if node.right == None:
                node.balance = 1
                return { "balance": 1, "direction": "L" }
            else:
                node.balance = 0
                return { "balance": 0, "direction": direction }
        elif node.data < data and node.right != None:
            direction = "R"
            res = self.inserter(node.right, data)
        elif node.data < data and node.right == None:
            node.right = Node(data)
            if node.left == None:
                node.balance = -1
                return { "balance": -1, "direction": "R" }
            else:
                node.balance = 0
                return { "balance": 0, "direction": direction }
        elif node.data == data:
            return { "balance": 0, "direction": direction }

        if res["balance"] == 0:
            return { "balance": 0, "direction": direction }
        if res["balance"] == 99:
            if direction == "L":
                node.left = res["node"]
            else:
                node.right = res["node"]
            return { "balance": 0, "direction": direction }
        if direction == "L":
            node.balance+=1
        else:
            node.balance-=1
        
        direction = direction + res["direction"]
        if node.balance >= 2 or node.balance <= -2:
            st = direction[:2]
            newNode = None
            if st == "LL":
                newNode = self.LLRotation(node)
            elif st == "RR":
                newNode = self.RRRotation(node)
            elif st == "LR":
                newNode = self.LRRotation(node)
            elif st == "RL":
                newNode = self.RLRotation(node)
            self.balancer(newNode)
            return { "balance": 99, "direction": direction, "node": newNode }
        else:
            return { "balance": res["balance"], "direction": direction }

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            res = self.inserter(self.head, data)
            if res["balance"] == 99:
                self.head = res["node"]
        return

    def treePrinter(self, node, level = 1):
        if node.left:
            self.treePrinter(node.left, level+1)
        print("[ level: ", level, "Data: ", node.data, "Balance: ", node.balance, "]")
        if node.right:
            self.treePrinter(node.right, level+1)

bt = AVLTree()
bt.insert(30)
bt.insert(10)
bt.insert(5)
bt.insert(8)
bt.insert(7)
bt.insert(3)
bt.insert(9)
bt.insert(11)
bt.insert(1)
bt.treePrinter(bt.head)