'''
Max Sum Contiguous Subarray
we can use here :-
1. brute force
2. divide and conquer
3. kadane's algo
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray1(self, A):
        maxSum = -99999999999
        ln = len(A)

        fullSum=0
        x=0
        while x<=ln-1:
            fullSum+=A[x]
            x+=1

        for i in range(ln):
            sm = fullSum
            for j in range(ln-1,i-1,-1):
                try:
                    sm-=A[j+1]
                except:
                    sm=fullSum
                if sm>maxSum:
                    maxSum = sm
            fullSum-=A[i]
        return maxSum

ans = Solution().maxSubArray1([22,-4,-3,4,-1,2,1,-5,4])
print(ans)