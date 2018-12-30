class LinkedList:
    def __init__(self, arr):
        self.list = {
            "value": arr[0],
            "next": None
        }
        self.arr = arr
        self.leng = len(arr)
        self.list["next"] = self.listCreator(0)

        print("self.list: ", self.list)

    def listCreator(self, i):
        i = i+1
        if i>self.leng-1:
            return None
        return {
            "value": self.arr[i],
            "next": self.listCreator(i)
        }

# LinkedList([1,2,3,4])