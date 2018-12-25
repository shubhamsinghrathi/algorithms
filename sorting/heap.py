'''
Task list:
- create incremental heap in array format
- add element to heap
- remove element from heap
- search element in heap
'''

class HeapDS:
    def __init__(self, unsorted):
        self.unsorted = unsorted
        self.heap = []
        self.length = 0
        self.createHeap()
        print("self.unsorted: ", self.unsorted)
        print("self.heap: ", self.heap)

    def createHeap(self):
        ln = len(self.unsorted)
        while self.length < ln:
            self.heap.append(self.unsorted[self.length])
            childNode = self.length
            parentNode = int((self.length - 1)/2)
            if self.length != 0:
                self.heapify(childNode, parentNode)
            self.length = self.length + 1

    def heapify(self, childNode, parentNode):
        if(self.heap[parentNode] < self.heap[childNode]):
            self.heap[parentNode], self.heap[childNode] = (self.heap[childNode], self.heap[parentNode])
            if parentNode != 0:
                childNode = parentNode
                parentNode = int((childNode - 1)/2)
                self.heapify(childNode, parentNode)
            return
        return

    def insert(self, item):
        self.heap.append(item)
        childNode = self.length
        parentNode = int((self.length - 1)/2)
        if self.length != 0:
            self.heapify(childNode, parentNode)
        self.length = self.length + 1
        print("self.heap: ", self.heap)

    def delete(self, place):
        self.heap[place] = self.heap[self.length-1]
        self.heap.pop()
        self.length = self.length - 1
        parentNode = place
        childNode = (2*parentNode) + 1
        if childNode < self.length:
            self.deletify(childNode, parentNode)
        print("self.heap: ", self.heap)

    def deletify(self, childNode, parentNode):
        if (childNode+1 < self.length):
            #means praent have left and right both children
            if self.heap[childNode + 1] > self.heap[childNode]:
                childNode = childNode + 1

        if(self.heap[parentNode] < self.heap[childNode]):
            self.heap[parentNode], self.heap[childNode] = (self.heap[childNode], self.heap[parentNode])
            parentNode = childNode
            childNode = (2*parentNode) + 1
            if childNode < self.length:
                self.deletify(childNode, parentNode)
            return
        return

    def search(self, item):
        self.itemToSearch = item
        self.found = False
        self.itemLocation = -1
        self.searchify(0, False)
        print("item: ", item, "found: ", self.found, "itemLocation: ", self.itemLocation)

    def searchify(self, parent, left=True):
        if self.heap[parent] == self.itemToSearch:
            self.found = True
            self.itemLocation = parent
            return
        if self.itemToSearch > self.heap[parent]:
            if parent + 1 < self.length and left == True:
                self.searchify(parent + 1, False)
            return

        if ((2*parent)+1) < self.length:
            self.searchify((2*parent)+1)
        if parent + 1 < self.length and left == True:
            self.searchify(parent + 1, False)

hs = HeapDS([ 4, 10, 3, 5, 1, 12, 19, 2, 5 ])
# hs.insert(11)
# hs.delete(1)
hs.search(4)
hs.search(5)
hs.search(12)
hs.search(19)
hs.search(3)
hs.search(1)
hs.search(11)
hs.search(211)
hs.search(-1)