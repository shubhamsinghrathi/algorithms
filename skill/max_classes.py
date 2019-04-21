# 2
# 4
# Maths 16:00 18:00
# ComputerScience 12:00 13:00
# Physics 12:30 14:00
# Chemistry 14:00 16:00
# 5
# Geography 14:00 16:00
# History 12:00 14:30
# Arts 14:00 16:30
# Literature 12:30 13:30
# German 13:30 15:00

def swap(arr, p1, p2):
    arr[p1], arr[p2] = (arr[p2], arr[p1])

class HeapEle:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class MinHeap:
    def __init__(self):
        self.heap = []
        self.length = 0

    def insertBalancer(self, pos):
        if pos==0:
            return
        pp = pos//2
        if self.heap[pp].end >self.heap[pos].end:
            swap(self.heap, pp, pos)
            self.insertBalancer(pp)
        else:
            return

    def insert(self, ele):
        self.heap.append(ele)
        self.length+=1
        if self.length==1:
            return
        self.insertBalancer(self.length-1)

    def deleteBalancer(self, pos):
        lc = (pos+1)*2 - 1
        rc = lc + 1
        if lc>self.length-1:
            return
        elif rc>self.length-1:
            if self.heap[pos].end>self.heap[lc].end:
                swap(self.heap, pos, lc)
                return
        else:
            ps=rc
            if self.heap[rc].end>self.heap[lc].end:
                ps=lc
            if self.heap[pos].end>self.heap[ps].end:
                swap(self.heap, pos, ps)
                self.deleteBalancer(ps)

    def pop(self):
        if self.length==0:
            return None
        res = self.heap[0]
        self.length-=1
        swap(self.heap, 0, self.length)
        self.deleteBalancer(0)
        return res

# mH = MinHeap()
# e1 = HeapEle(0, 4)
# e2 = HeapEle(0, 2)
# e3 = HeapEle(0, 1)
# e4 = HeapEle(0, 7)
# e5 = HeapEle(0, 6)
# mH.insert(e1)
# mH.insert(e2)
# mH.insert(e3)
# mH.insert(e4)
# mH.insert(e5)
# print(mH.pop())
# print(mH.pop())
# print(mH.pop())
# print(mH.pop())
# print(mH.pop())
# print(mH.pop())
# print(mH.pop())
# print(mH.pop())

def main():
    days = int(input())
    outputs = []
    for i in range(days):
        n = int(input())
        mH = MinHeap()
        for x in range(n):
            ip = input().split()
            s1 = ip[1].split(":")
            start = int(s1[0]+s1[1])
            e1 = ip[2].split(":")
            end = int(e1[0]+e1[1])
            mH.insert(HeapEle(start, end))
        val = mH.pop()
        lastPop = None
        totalSubjects = 0
        while val:
            if not lastPop:
                lastPop = val
                totalSubjects+=1
                val = mH.pop()
                continue
            if val.start>=lastPop.end:
                totalSubjects+=1
                lastPop = val
            val = mH.pop()
        outputs.append(totalSubjects)
    for i in outputs:
        print("totalSubjects: ", i)

main()