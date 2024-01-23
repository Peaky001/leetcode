class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s)-1
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j-=1
        return s