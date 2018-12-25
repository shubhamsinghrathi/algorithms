'''
Task list:
- do sorting using heap
'''

from heap import *

sortedArr = []
def heapSort(arr):
    hds = HeapDS(arr)
    for i in range(0, len(hds.heap)):
        sortedArr.append(hds.heap[0])
        hds.heap[0] = hds.heap[hds.length - 1]
        hds.length = hds.length - 1
        hds.deletify(1, 0)
    print("sortedArr: ", sortedArr)

heapSort([ 4, 10, 3, 5, 1, 12, 19, 2, 5, 50, 65, 21, 9, 31, -8, -2, -1 ])