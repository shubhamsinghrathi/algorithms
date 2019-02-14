def insertionSort(arr):
    for x in range(1, len(arr)):
        pos = x
        ele = arr[x]
        while x>0 and arr[x-1]>ele:
            arr[x], arr[x-1] = (arr[x-1], arr[x])
            x-=1
        arr[x]=ele
    print(arr)

insertionSort([3,2,4,5,1,9,10,11])