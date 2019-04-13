class MaxHeap:
    def __init__(self, arr):
        self.treeArr = arr
        self.size = len(arr)
        self.heapGenerator()
    
    def swapper(self, p1, p2):
        self.treeArr[p1], self.treeArr[p2] = (self.treeArr[p2], self.treeArr[p1])

    def popAdjust(self, pp):
        lcp = 2*pp
        rcp = lcp+1
        if lcp>self.size:
            return
        if rcp>self.size:
            if self.treeArr[pp-1] < self.treeArr[lcp-1]:
                self.swapper(pp-1, lcp-1)
                return
            else:
                return
        pt = rcp
        if self.treeArr[lcp-1] > self.treeArr[rcp-1]:
            pt = lcp
        if self.treeArr[pp-1] < self.treeArr[pt-1]:
            self.swapper(pp-1, pt-1)
            self.popAdjust(pt)
        else:
            return

    def heapGenerator(self):
        for i in range(self.size, 0, -1):
            self.popAdjust(i)

    def pop(self):
        if self.size == 0:
            return None
        to_return = self.treeArr[0]
        self.size-=1
        self.treeArr[0], self.treeArr[self.size] = (self.treeArr[self.size], self.treeArr[0])
        self.popAdjust(1)
        return to_return

mh = MaxHeap([1,3,2,4,5,22,65,31,4,9])
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())