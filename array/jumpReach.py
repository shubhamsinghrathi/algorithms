import math

def diffBetweenTwoElements(d1, d2):
    eles = []
    if d1>d2:
        eles.append(d2)
        v = d1%d2
        if v==d2:
            eles.append(d1)
        elif v>0:
            eles.append(v)
            eles.append(d1)
    else:
        eles.append(d1)
        v = d2%d1
        if v==d1:
            eles.append(d2)
        elif v>0:
            eles.append(v)
            eles.append(d2)
    return eles

def jumpReach(arr, k, d1, d2):
    eleArr = diffBetweenTwoElements(d1, d2)
    resArr = []
    for val in arr:
        if val == k:
            resArr.append(1)
        else:
            c1 = math.fabs(k-d1)
            c2 = math.fabs(k-d2)
            if val == (k-d1) or val == (d1-k) or val == (k-d2) or val == (d2-k):
                resArr.append(1)
            else:
                