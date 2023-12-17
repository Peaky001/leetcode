class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
       my_length = len(candyType)
       eatable = my_length//2
       set_candytype = set(candyType)
       if eatable<= len(set_candytype):
           return eatable
       elif eatable > len(set_candytype):
           return len(set_candytype)