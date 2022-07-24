class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = str(a)
        d = str(b)
        
        num = int(c,2) +int(d,2)
        return bin(num)[2:]
       
        a = int(input())
        b = int(input())
        
        result = addBinary(a,b)
        print(result)
        