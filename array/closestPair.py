'''
Given a sorted array and a number x, find the pair in array whose sum is closest to x
'''

import math

def closestPair(arr, value):
    startLimit = 0
    topLimit = len(arr)
    pair = [arr[0], arr[1]]
    totalSum = arr[0] + arr[1]

    if arr[-1] + arr[-2] <= value:
        print("pair1: ", [arr[-2], arr[-1]])
        return
    while True:
        if topLimit < startLimit+1:
            break
        item1 = arr[startLimit]
        for i in range(startLimit+1, topLimit):
            item2 = arr[i]
            tempSum = item1 + item2
            if (math.fabs(totalSum - value) < math.fabs(tempSum - value)) and (tempSum - value) > 0:
                topLimit = i
                break
            elif (tempSum - value) <= 0:
                totalSum = tempSum
                pair = [item1, item2]
            # print("tempSum: ", tempSum, item1, item2, pair, topLimit)

        startLimit = startLimit + 1
    print("pair: ", pair)
        # print("startLimit+1: ", startLimit+1, topLimit)

closestPair([1, 3, 4, 7, 10], 15)
closestPair([10, 22, 28, 29, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 54)