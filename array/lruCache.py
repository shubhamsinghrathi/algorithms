'''
Least recently used cache
'''

class LRUCache:
    def __init__(self, length=10):
        self.maxLength = length
        self.length = 0 #current length of the cache
        self.cache = {}
        self.lastElement = None

    def addElement(self, value):
        if self.length == 0:
            self.cache = {
                "data": value,
                "next": None,
                "prev": None
            }
            self.lastElement = self.cache
            self.length = 1
        elif self.length < self.maxLength:
            # self.lastElement["next"] = {
            #     "data": value,
            #     "next": None,
            #     "prev": self.lastElement
            # }
            # self.length = self.length + 1
            self.cache = {
                "data": value,
                "next": self.cache,
                "prev": None
            }
            if self.length == 1:
                self.lastElement["prev"] = self.cache
            self.cache["next"]["prev"] = self.cache
            self.length = self.length + 1
        else:
            self.lastElement = self.lastElement["prev"]
            self.lastElement["next"] = None
            self.cache = {
                "data": value,
                "next": self.cache,
                "prev": None
            }
            self.cache["next"]["prev"] = self.cache
    
    def fetchElement(self, value):
        cache = self.cache
        while True:
            if cache["data"] == value:
                self.cache = {
                    "data": cache["data"],
                    "next": self.cache,
                    "prev": None
                }
                self.cache["next"]["prev"] = self.cache
                if cache["prev"] == None:
                    cache["prev"] = self.cache
                temp = cache["prev"]
                cache["prev"]["next"] = cache["next"]
                cache["next"]["prev"] = temp
                return cache["data"]
            if cache["next"] == None:
                break
            cache = cache["next"]
        return "Not found"

    def printCache(self):
        print("cache: ", self.cache)

lru = LRUCache(5)
lru.addElement(1)
lru.addElement(2)
lru.addElement(3)
lru.addElement(4)
lru.addElement(5)
lru.addElement(6)

z = lru.fetchElement(4)
z = lru.fetchElement(6)
# print("z: ", z)
lru.printCache()