import numpy as np

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(np.sqrt(x))

sol=Solution().mySqrt(8)
print(sol)