'''
this data-structure better for graph representation than the adjacency matrixs.
To store the nodes with each vertex, it is not necessary to use linked list, we can use binary tree or heap too, for better search, insert, delete etc.
'''
from queue import *

class AdjacencyList:
    def __init__(self, isDirected=False):
        self.vertexs = {}
        self.degree = {} #degree of each vertex
        self.totalVertexes = 0
        self.totalEdges = 0
        self.isDirected = isDirected

    def addVertex(self, value):
        try:
            self.vertexs[value]
            print("Invalid vertex provided")
            return
        except:
            self.vertexs[value] = [] #for simplecity, I am using array here, for better perfromance, use binary tree here
            self.totalVertexes = self.totalVertexes + 1
            self.degree[value] = 0
            return

    def addEdge(self, v1, v2):
        try:
            self.vertexs[v1]
            self.vertexs[v2]
        except:
            print("Invalid edge provided")
            return
        found = False
        for val in self.vertexs[v1]:
            if val == v2:
                found = True
                print("Edge already found")
                break
        if found == False:
            self.vertexs[v1].append(v2)
            self.totalEdges = self.totalEdges + 1
            self.degree[v1] = self.degree[v1] + 1
            if self.isDirected == False:
                self.vertexs[v2].append(v1)
                self.totalEdges = self.totalEdges + 1
                self.degree[v2] = self.degree[v2] + 1

    def removeVertex(self, value):
        try:
            self.vertexs[value]
        except:
            print("Invalid vertex was provided")
            return

        otherVertexs = self.vertexs.pop(value)
        self.totalVertexes = self.totalVertexes - 1
        self.totalEdges = self.totalEdges - len(otherVertexs)

        if self.isDirected == False:
            self.totalEdges = self.totalEdges - len(otherVertexs)
            for val in otherVertexs:
                self.vertexs[val].remove(value)
        else:
            for val in list(self.vertexs.keys()):
                try:
                    self.vertexs[val].remove(value)
                    self.totalEdges = self.totalEdges - 1
                except:
                    continue
    
    def removeEdge(self, v1, v2):
        try:
            self.vertexs[v1]
            self.vertexs[v2]
        except:
            print("Invalid edge provided")
            return

        try:
            self.vertexs[v1].remove(v2)
            self.totalEdges = self.totalEdges - 1
            if self.isDirected == False:
                self.vertexs[v2].remove(v1)
                self.totalEdges = self.totalEdges - 1
        except:
            print("Invalid edge provided...2")
            return

    def minDistanceBetweenTwoVertex(self, v1, v2):
        #FOR THIS I AM USING BFS
        try:
            self.vertexs[v1]
            self.vertexs[v2]
        except:
            print("Invalid vertexes were provided")
            return

        self.discovered = {}
        self.processed = {}
        self.shortestPath = []
        if v1 == v2:
            print("shortestPath: ", [v1])
            return [v1]
        self.queue = Queue()
        self.queue.push(v1)
        self.toFind = v2
        self.elementFound = False

        self.levels = {}
        self.vertexToLevel = {}
        self.levels[0] = [
            {
                "value": v1,
                "parent": None
            }
        ]
        self.vertexToLevel[v1] = 0

        self.pathFinder()
        if self.elementFound == True:
            # print("self.levels: ", self.levels)
            print("shortestPath: ", self.shortestPath)
        else:
            # print("not found", self.levels)
            print("both vertex are not connected")
    
    def pathFinder(self):
        value = self.queue.pop()
        if value == None:
            return
        self.processed[value] = True
        currentLevel = self.vertexToLevel[value] + 1
        try:
            self.levels[currentLevel]
        except:
            self.levels[currentLevel] = []

        for val in self.vertexs[value]:
            try:
                self.vertexToLevel[val]
            except:
                self.queue.push(val)
                self.levels[currentLevel].append({
                    "value": val,
                    "parent": value
                })
                self.vertexToLevel[val] = currentLevel
                if val == self.toFind:
                    self.elementFound = True
                    self.pathCreator(value, currentLevel, val)
                    break
        if self.elementFound == False:
            self.pathFinder()

    def pathCreator(self, parent, currentLevel, val):
        reversePath = [ val ]
        while currentLevel > 0:
            currentLevel = currentLevel - 1
            for val1 in self.levels[currentLevel]:
                if val1["value"] == parent:
                    reversePath.append(parent)
                    parent = val1["parent"]
                    break
        # print("reversePath: ", reversePath)
        for i in range(len(reversePath)-1, -1, -1):
            self.shortestPath.append(reversePath[i])

al = AdjacencyList(False)

al.addVertex(1)
al.addVertex(2)
al.addVertex(3)
al.addVertex(4)
al.addVertex(5)
al.addVertex(6)
al.addVertex(7)
al.addVertex(8)
al.addVertex(9)
al.addVertex(10)

al.addEdge(1,2)
al.addEdge(1,3)
al.addEdge(1,4)
al.addEdge(2,4)
al.addEdge(3,4)
al.addEdge(5,6)
al.addEdge(4,5)
al.addEdge(4,6)

al.addEdge(6,8)
al.addEdge(2,7)
al.addEdge(7,8)
al.addEdge(3,9)
al.addEdge(9,10)
al.addEdge(2,10)
# print(al.vertexs)

al.minDistanceBetweenTwoVertex(4, 1)