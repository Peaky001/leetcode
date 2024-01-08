class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
         stone_dict = collections.defaultdict(int)
         sum = 0
         for i in stones:
             stone_dict[i]+=1
         for j in jewels:
             if j in stone_dict:
                 sum+= stone_dict[j]
         return sum