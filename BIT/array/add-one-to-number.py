class Solution1:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        ln = len(A)
        number = 0
        j=0
        for i in range(ln-1, -1, -1):
            number += A[j] * 10**i
            j+=1
        number+=1
        ans = []
        while number>0:
            ans.insert(0, (number % 10))
            number = int(number/10)
        return ans




class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        ln = len(A)
        nm = A[ln-1]
        ans = []
        topNon9 = False
        all9=False
        if nm != 9:
            A[ln-1]+=1
        else:
            for i in range(ln-1, -1, -1):
                if A[i] == 9:
                    A[i]=0
                    if topNon9==False:
                        all9=True
                else:
                    A[i]+=1
                    topNon9 = True
                    all9=False
                    break
            if topNon9 == False:
                ans.append(1)

        nonZeroFound = False
        for i in range(ln):
            if nonZeroFound == False and A[i]!=0:
                ans.append(A[i])
                nonZeroFound = True
            elif nonZeroFound == True or all9==True:
                ans.append(A[i])
        return ans



# res = Solution().plusOne([ 0, 3, 7, 6, 4, 0, 5, 5, 5 ])
res = Solution().plusOne([ 9,9,9 ])
print(res)