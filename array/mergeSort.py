def mergeSort(arr):
    l = len(arr)
    n = int(l/2)
    if n>0:
        a1 = arr[:n]
        a2 = arr[n:]
        res1 = mergeSort(a1)
        res2 = mergeSort(a2)

        l1 = len(res1)
        l2 = len(res2)
        res = []
        m1=0
        m2=0
        while m1<l1 and m2<l2:
            if res1[m1]>=res2[m2]:
                res.append(res2[m2])
                m2+=1
            else:
                res.append(res1[m1])
                m1+=1
        for x in range(m1,l1):
            res.append(res1[x])
        for x in range(m2,l2):
            res.append(res2[x])
        return res
    return arr

arr = mergeSort([2,3,1,4,5,8,9,1,2])
print(arr)