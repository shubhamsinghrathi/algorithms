'''
sorts the directed acyclic graph(DAG) in topological order
'''
from AdjacencyList import *
import copy

class TopologicalSorting:
    def __init__(self):
        self.graph = AdjacencyList(True)
        self.graphPrepare()

    def graphPrepare(self):
        self.graph.addVertex(1)
        self.graph.addVertex(2)
        self.graph.addVertex(3)
        self.graph.addVertex(4)
        self.graph.addVertex(5)
        self.graph.addVertex(6)
        self.graph.addVertex(7)

        self.graph.addEdge(1,3)
        self.graph.addEdge(2,3)
        self.graph.addEdge(3,5)
        self.graph.addEdge(2,4)
        self.graph.addEdge(5,6)
        self.graph.addEdge(4,6)
        self.graph.addEdge(6,7)

    def initSorting(self):
        self.visited = {}
        self.reversedTopologicalArray = []
        self.topologicalArray = []
        self.allVertexes = self.graph.vertexs.keys()
        for key in self.allVertexes:
            try:
                self.visited[key]
                continue
            except:
                self.visited[key] = True
                self.dfs(key, 0)
                self.reversedTopologicalArray.append(key)
        self.topologicalArray = self.reversedTopologicalArray.copy()
        self.topologicalArray.reverse()

    def dfs(self, vertex, number=0):
        try:
            while True:
                value = self.graph.vertexs[vertex][number]
                try:
                    self.visited[value]
                    number = number + 1
                except:
                    self.visited[value] = True
                    self.dfs(value, 0)
                    self.reversedTopologicalArray.append(value)
                    break
        except:
            return None

ts = TopologicalSorting()
ts.initSorting()
print("reversedTopologicalArray: ",  ts.reversedTopologicalArray)
print("topologicalArray: ",  ts.topologicalArray)