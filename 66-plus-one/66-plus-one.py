class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        my_num = int("".join(str(i) for i in digits))
        my_num+=1
        
        
        
        
        return [ int(j) for j in str(my_num)]
    
        
        
        my_list = list(map(int,input().split()))
        
        result = plusOne(my_list)
        print(result)
        
        
        