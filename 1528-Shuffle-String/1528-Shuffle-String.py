class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result_string =""
       
        for i in range(len(s)):
            result_string  += s[indices.index(i)]
            
        return result_string
