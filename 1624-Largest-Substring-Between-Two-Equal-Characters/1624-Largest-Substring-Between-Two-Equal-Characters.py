class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    result= max(result,j-i-1)
        return(result)