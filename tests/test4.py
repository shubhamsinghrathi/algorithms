class Solution:
    def climbStairs(self, n):
        if n<=1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

sl = Solution()
print(sl.climbStairs(6))