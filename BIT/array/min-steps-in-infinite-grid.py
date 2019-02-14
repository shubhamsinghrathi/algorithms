'''
min steps in infinite grid
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        minSteps = 0
        for i in range(len(A)-1):
            diff1 = abs(A[i]-A[i+1])
            diff2 = abs(B[i]-B[i+1])
            if diff1>diff2:
                minSteps += diff1
            else:
                minSteps += diff2
        return minSteps

steps = Solution().coverPoints([0, 1, 1], [0, 1, 2])
print("steps: ", steps)