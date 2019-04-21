#0 1 1 2 3 5 8 13 21 34 ...

catch = {}

def fibonacci(n):
    try:
        return catch[n]
    except:
        if n<2:
            catch[n]=n
            return n
        catch[n]=fibonacci(n-1) + fibonacci(n-2)
        return catch[n]

print(fibonacci(50))
print(fibonacci(31))
print(fibonacci(25))
print(fibonacci(27))
print(fibonacci(29))
print(fibonacci(31))