def taylorOutput(x,n):
    res = result(x, n)
    print(res[0])

def result(x, n):
    if n<=0:
        return [1,1]
    v = result(x, n-1)
    vl = (x/n) * v[1]
    return [ v[0]+vl, vl ]

taylorOutput(2,3)