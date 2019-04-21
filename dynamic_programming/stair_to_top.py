'''
Problem statement:  You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution procedure: We are using dynamic programming, where we are using catching of old and smaller results
So, when we have "n" stairs then the person can climb "1" or "2" stair at that time. Hence, the total ways
to react to the top when left stairs are "n" will be the sum of stair to reach to top when lefted stairs are
"n-1" (if user took 1 step) and "n-2" (if user took 2 steps).
And if n==0 or 1 then required steps will be 1 in either case because for n="0" he has reached and n="1" he can 
take only 1 step
'''

catch = {}

def stairPaths(n):
    try:
        return catch[n]
    except:
        if n==0 or n==1:
            catch[n]=1
            return catch[n]
        catch[n]=stairPaths(n-1)+stairPaths(n-2)
        return catch[n]

print(stairPaths(6))