from linked_list import LinkedList

ll = LinkedList()
ll.add("aaaa")
ll.add("bbbb")
ll.add("cccc")
ll.add("dddd")
ll.add("eeee")
ll.printList()

class llReverser:
    def __init__(self, ll):
        self.ll = ll
        self.list = {}
        self.reverser()

    def reverser(self):
        currentNext = self.ll["next"]
        currentData = self.ll["data"]
        newNext = None
        while currentNext != None:
            newNext = {
                "data": currentData,
                "next": newNext
            }  
            currentData = currentNext["data"]
            currentNext = currentNext["next"]
        self.list = {
            "data": currentData,
            "next": newNext
        }

    def printList(self):
        print(self.list)

lr = llReverser(ll.list)
lr.printList()