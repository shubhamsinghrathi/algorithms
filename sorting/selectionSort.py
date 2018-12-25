def selectionSortAsc(arr):
    print('arr: ', arr)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j]<arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print('Sorted arr (asc): ', arr)

selectionSortAsc([1,4,7,2,6,3,8,9,5])

'''
loop invarient for this sorting machanish is that, for every subarray of 'i' length this array is always sorted
'''