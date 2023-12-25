class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        res = set.intersection(*map(set,nums))
        return sorted(res)