'''
This quicksort algo is written using the same array
'''

def quickSort(arr,start=0,end=-1):
    if end==-1:
        end = len(arr)-1
    if start >= end:
        return
    pivot = arr[end]
    sp = start #start position
    ep = end #end position
    pos = end
    for x in range(sp, ep+1):
        if (arr[x]>pivot and pos>x):
            arr[x], arr[pos] = (arr[pos], arr[x])
            pos = x
        elif (arr[x]<pivot and pos<x):
            arr[x], arr[pos+1] = (arr[pos+1], arr[x])
            arr[pos], arr[pos+1] = (arr[pos+1], arr[pos])
            pos+=1
    quickSort(arr, start, pos-1)
    quickSort(arr, pos+1, end)

arr = [2,7,1,4,5]
quickSort(arr)
print(arr)