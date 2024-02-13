class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for palindrom_string in words:
            if(palindrom_string==palindrom_string[::-1]):
                return palindrom_string
        return ""