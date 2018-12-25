'''
finding the Kth smallest element from the array using quick select which is based on quich sort DS.
'''
####NOTE, I'THINK THAT IT IS QUICK SELECT ALGO, BUT IT MAY BE EVEN BETTER

class quickSelect:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        self.total = 0
        self.quickMod()
        print("answer: ", self.answer)

    def quickMod(self):
        lastQs = None
        self.answer = None
        while True:
            lastQs = self.sorter(self.arr)
            print("self.total: ", self.total)
            if lastQs["middle"] == True:
                self.answer = lastQs["main"]
                break
            else:
                if lastQs["right"] == True:
                    self.total = self.total + 1 #bcz, main element will also be counted now
                    self.arr = lastQs["rightArr"]
                else:
                    self.total = self.total - len(lastQs["leftArr"])
                    self.arr = lastQs["leftArr"]

    def sorter(self, elements):
        ln = len(elements)
        qs = {
            "main": None,
            "leftArr": [],
            "rightArr": [],
            "middle": False,
            "left": False,
            "right": False
        }
        if ln == 0:
            return qs
        qs["main"] = elements[ln-1]
        if ln == 1:
            qs["middle"] = True
            return qs
        for i in range(0, ln-1):
            if elements[i] <= qs["main"]:
                qs["leftArr"].append(elements[i])
                self.total = self.total + 1
            else:
                qs["rightArr"].append(elements[i])

        if self.total == self.k - 1:
            qs["middle"] = True
        elif self.total > self.k - 1:
            qs["left"] = True
        elif self.total < self.k - 1:
            qs["right"] = True

        return qs

quickSelect([5, 9, 10, 1, 3, 8, 12, 7], 3)