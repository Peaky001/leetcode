class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        joined_list  = s.split(" ")
        return " ".join(joined_list[:k])