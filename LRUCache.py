#Least recently used cache has a max size.
#It should fastly fetch O(1) and fastly add O(1) items
#We must implement fast search and fast removal in this data structure
#We know that HashTable shows fast fetch and Double Linked List show fast removal
#So, I'm using them both here

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, maxSize=5):
        self.maxSize = maxSize
        self.size = 0
        self.start = None
        self.end = None
        self.hashTable = {}

    def push(self, key, value):
        try:
            self.hashTable[key].value = value
            self.get(key)
            return
        except:
            pass
        if self.size < self.maxSize:
            self.size+=1
            fVal = self.start
            self.start = Node(key, value)
            if not self.end:
                self.end = self.start
            else:
                self.start.next = fVal
                fVal.prev = self.start
            self.hashTable[key] = self.start
            return
        lVal = self.end
        self.end = self.end.prev
        self.end.next = None
        del self.hashTable[lVal.key]

        fVal = self.start
        self.start = Node(key, value)
        self.start.next = fVal
        fVal.prev = self.start
        self.hashTable[key] = self.start
        return

    def get(self, key):
        try:
            val = self.hashTable[key]
        except:
            return None
        fVal = self.start
        if fVal == val:
            return val.value
        leftNode = val.prev
        rightNode = val.next
        if leftNode and rightNode:
            leftNode.next = rightNode
            rightNode.prev = leftNode
        elif leftNode:
            leftNode.next = None
            self.end = leftNode
        self.start = val
        val.prev = None
        self.start.next = fVal
        fVal.prev = self.start
        return val.value

cache = LRUCache(4)
cache.push("a", "A_____99")
cache.push("b", "B_____99")
cache.push("c", "C_____99")
cache.push("d", "D_____99")
cache.push("a", "AA_____99")
cache.push("e", "E_____99")
print(cache.get("a"))
print(cache.get("b"))
print(cache.get("c"))
print(cache.get("d"))
print(cache.get("e"))