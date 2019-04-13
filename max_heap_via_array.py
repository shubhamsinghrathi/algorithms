import math

class MaxHeap:
    def __init__(self):
        self.treeArr = []
        self.size = 0

    def pushAdjust(self, cp):
        if cp == 1:
            return
        pp = math.floor(cp/2)
        if self.treeArr[pp-1] < self.treeArr[cp-1]:
            self.treeArr[pp-1], self.treeArr[cp-1] = (self.treeArr[cp-1], self.treeArr[pp-1])
        self.pushAdjust(pp)

    def push(self, data):
        self.treeArr.append(data)
        self.size+=1
        self.pushAdjust(self.size)

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

    def pop(self):
        if self.size == 0:
            return None
        to_return = self.treeArr[0]
        self.size-=1
        self.treeArr[0], self.treeArr[self.size] = (self.treeArr[self.size], self.treeArr[0]) ### here this could also use to make the same array sorted as we pop the items from top
        ###the upper line implements heap sort
        self.popAdjust(1)
        return to_return


############## normal method of heap creation take O(n log n) time, but heapify process (where we go from inserting last to first element OR opposite direction) takes only O(n) time.


mh = MaxHeap()
mh.push(5)
mh.push(25)
mh.push(15)
mh.push(7)
mh.push(10)
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())
print(mh.pop())