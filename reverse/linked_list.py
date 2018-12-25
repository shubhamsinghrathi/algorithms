class LinkedList:
    def __init__(self):
        self.list = {}
        self.initialized = False

    def add(self, data):
        if self.initialized == False:
            self.list = {
                "data": data,
                "next": None
            }
            self.initialized = True
        else:
            item = {
                "data": data,
                "next": None
            }
            theList = self.traverse(self.list)
            theList["next"] = item

    def traverse(self, theList):
        if theList["next"] == None:
            return theList
        else:
            return self.traverse(theList["next"])

    def printList(self):
        print(self.list)