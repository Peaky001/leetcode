class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        count = collections.Counter(nums)
        for i in count:
            if count[i]>1:
                result += count[i]*(count[i]-1)//2
        return result
        