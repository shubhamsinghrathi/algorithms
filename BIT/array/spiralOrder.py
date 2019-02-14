class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        c=len(A[0])
        r=len(A)
        t=0
        b=r-1
        l=0
        r=c-1
        ans=[]

        drxn=1
        while t<=b and l<=r:
            if drxn==1:
                for x in range(l, r+1):
                    ans.append(A[t][x])
                t+=1
                drxn=2
            elif drxn==2:
                for x in range(t, b+1):
                    ans.append(A[x][r])
                r-=1
                drxn=3
            elif drxn==3:
                for x in range(r, l-1, -1):
                    ans.append(A[b][x])
                b-=1
                drxn=4
            else:
                for x in range(b, t-1, -1):
                    ans.append(A[x][l])
                l+=1
                drxn=1
        print("ans: ", ans)

Solution().spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10, 11, 12]
])