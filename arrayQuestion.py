#replace-element-array-product-every-element-without-using-division-operator

arr = [1,2,3,4,5]

leng = len(arr)

def theFunc(arr, num):
    if num >= leng:
        return
    ele = arr[num]
    arr[num] = 1
    theFunc(arr, num+1)
    for i in range(0, leng):
        if num != i:
            arr[i] *= ele

theFunc(arr, 0)
print("arr: ", arr)