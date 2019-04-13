def swap(arr, p1, p2):
    arr[p1], arr[p2] = (arr[p2], arr[p1])

def divider(arr, sp, lp):
    if lp-sp<1:
        return
    i = sp
    j = lp
    pivot = arr[sp]
    while j>i:
        while (arr[i]<=pivot) and (i<lp):
            i+=1
        while (arr[j]>pivot) and (j>sp):
            j-=1
        if i<j:
            swap(arr, i, j)
    swap(arr, sp, j)
    divider(arr, sp, j-1)
    divider(arr, j+1, lp)

def quickSort(arr):
    divider(arr, 0, len(arr)-1)
    print(arr)

quickSort([1,3,2,4,5,22,65,31,4,9])