class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if(y==x):
            return True
        else:
            return False
        
        
        
        
        
    