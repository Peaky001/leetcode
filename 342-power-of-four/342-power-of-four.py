import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if(n>0):
            return math.log(n,4).is_integer()
        else:
            False
        
        
        
        
        
        
        
