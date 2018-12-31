'''
provide the color to the vertex so that two vertex connected by edge won't have same color. Use minimum color.
this can be done with the help of bfs and some trick
'''
from AdjacencyList import *
from queue import *

class GraphColoring:
    def __init__(self, startVertex=1):
        self.graph = AdjacencyList(False)
        self.graphPrepare()
        self.startVertex = startVertex

    def graphPrepare(self):
        # self.graph.addVertex(1)
        # self.graph.addVertex(2)
        # self.graph.addVertex(3)
        # self.graph.addVertex(4)
        # self.graph.addVertex(5)
        # self.graph.addVertex(6)
        # self.graph.addVertex(7)
        # self.graph.addVertex(8)
        # self.graph.addVertex(9)
        # self.graph.addVertex(10)

        # self.graph.addEdge(1,2)
        # self.graph.addEdge(1,3)
        # self.graph.addEdge(1,4)
        # self.graph.addEdge(2,4)
        # self.graph.addEdge(3,4)
        # self.graph.addEdge(5,6)
        # self.graph.addEdge(4,5)
        # self.graph.addEdge(4,6)
        # self.graph.addEdge(6,8)
        # self.graph.addEdge(2,7)
        # self.graph.addEdge(7,8)
        # self.graph.addEdge(3,9)
        # self.graph.addEdge(9,10)
        # self.graph.addEdge(2,10)



        # self.graph.addVertex(1)
        # self.graph.addVertex(2)
        # self.graph.addVertex(3)
        # self.graph.addVertex(4)
        # self.graph.addVertex(5)
        # self.graph.addVertex(6)

        # self.graph.addEdge(1,2)
        # self.graph.addEdge(1,3)
        # self.graph.addEdge(1,4)
        # self.graph.addEdge(1,6)
        # self.graph.addEdge(2,3)
        # self.graph.addEdge(2,4)
        # self.graph.addEdge(2,5)
        # self.graph.addEdge(3,4)
        # self.graph.addEdge(3,5)
        # self.graph.addEdge(4,5)
        # self.graph.addEdge(5,6)



        self.graph.addVertex(1)
        self.graph.addVertex(2)
        self.graph.addVertex(3)
        self.graph.addVertex(4)
        self.graph.addVertex(5)
        self.graph.addVertex(6)
        self.graph.addVertex(7)
        self.graph.addVertex(8)
        self.graph.addVertex(9)

        self.graph.addEdge(1,2)
        self.graph.addEdge(1,4)
        self.graph.addEdge(2,5)
        self.graph.addEdge(2,3)
        self.graph.addEdge(3,6)
        self.graph.addEdge(4,5)
        self.graph.addEdge(4,7)
        self.graph.addEdge(5,6)
        self.graph.addEdge(5,8)
        self.graph.addEdge(6,9)
        self.graph.addEdge(7,8)
        self.graph.addEdge(8,9)

    def colorGraph(self):
        self.colorObj = {}
        self.totalColor = 1
        self.reachedVertex = {}
        self.queue = Queue()
        self.queue.push(self.startVertex)
        self.reachedVertex[self.startVertex] = True
        self.colorObj[self.startVertex] = {
            "parent": None,
            "color": self.totalColor
        }
        self.colorAssigner()

    def colorAssigner(self):
        value = self.queue.pop()
        if value == None:
            return
        parentColor = self.colorObj[value]["color"]
        foundColor = {}
        for val in self.graph.vertexs[value]:
            try:
                color = self.colorObj[val]["color"]
                foundColor[color] = True
                if color == parentColor:
                    for i in range(1, self.totalColor+2):
                        try:
                            foundColor[i]
                        except:
                            parentColor = self.colorObj[value]["color"] = i
                            if self.totalColor < i:
                                self.totalColor = i
                            break
            except:
                color = 1
                if parentColor == 1:
                    color = 2
                    if self.totalColor < 2:
                        self.totalColor = 2
                self.colorObj[val] = {
                    "parent": value,
                    "color": color
                }
                foundColor[color] = True
                self.queue.push(val)
        self.colorAssigner()

gc = GraphColoring(1)
gc.colorGraph()
# print("colorObj: ", gc.colorObj)
print("totalColor: ", gc.totalColor, 1)

gc = GraphColoring(2)
gc.colorGraph()
print("totalColor: ", gc.totalColor, 2)