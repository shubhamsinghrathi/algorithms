### to do this, we'll use BFS (and BFS require queue)
## Note - this is a bidirectional and unweighted graph
# Note - Actual path is not found yet because that would need backtracking

from queue import Queue

class SortestPath:
    def __init__(self, node=[], edges=[]):
        self.nodes = {}
        self.processed = {}
        self.totalSortestPaths = {}
        self.sortestLength = 99999999999
        self.queue = None
        for i in node:
            self.nodes[i] = []
        for e in edges:
            self.nodes[e[0]].append(e[1])
            self.nodes[e[1]].append(e[0])

    def doBFS(self, node):
        num = self.processed[node]
        crrNum = num+1
        nodes = self.nodes[node]
        for n in nodes:
            if n == self.target:
                if crrNum<self.sortestLength:
                    self.sortestLength = crrNum
                try:
                    self.totalSortestPaths[crrNum]+=1
                except:
                    self.totalSortestPaths[crrNum] = 1
            else:
                try:
                    self.processed[n]
                except:
                    self.processed[n] = crrNum
                    self.qu.push(n)
        while True:
            node = self.qu.pop()
            print("node: ", node)
            if not node:
                break
            self.doBFS(node)

    def sortestPathLengthAndTotalNumber(self, points):
        self.processed = {}
        self.target = points[1]
        self.totalSortestPaths = {}
        self.sortestLength = 99999999999
        self.qu = Queue()
        self.qu.push(points[0])
        self.processed[points[0]] = 0
        node = self.qu.pop()
        self.doBFS(node)
        print("sortestLength: ", self.sortestLength)
        print("totalSortestPaths: ", self.totalSortestPaths)

sp = SortestPath([1,2,3,4,5], [ [1,2], [1,3], [1,4], [2,5], [3,5], [4,5] ])
sp.sortestPathLengthAndTotalNumber([3,4])