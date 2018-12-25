def insertionSortAsc(arr):
    i=1
    max=len(arr)
    print('arr: ', arr)
    
    while(i<max):
        val = arr[i]
        j = i-1
        while j>-1 and arr[j]>val:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = val
        i = i+1
    
    print('sorted arr (asc): ', arr)

def insertionSortDes(arr):
    i = 1
    print('arr: ', arr)
    
    while(i < len(arr)):
        j = i-1
        val = arr[i]
        while val>arr[j] and j>-1:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = val
        i = i+1

    print('sorted arr (des): ', arr)

def insertionSortNewAsc(arr):
    ln = len(arr)
    i=1
    while(i<ln):
        j=i
        while(j>0 and arr[j]<arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
        i+=1
    print("sorted array: ", arr)

# insertionSortAsc([1,4,7,2,6,3,8,9,5])
# insertionSortDes([1,4,7,2,6,3,8,9,5])
insertionSortNewAsc([1,4,7,2,6,3,8,9,5])