class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2

        return self.climbStairs(n-1)+self.climbStairs(n-2)


sol=Solution().climbStairs(3)
print(sol)


