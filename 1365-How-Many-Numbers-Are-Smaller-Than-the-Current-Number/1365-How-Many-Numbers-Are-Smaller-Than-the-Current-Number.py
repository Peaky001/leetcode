class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        the_list = []
        D = {}
        for key,value in enumerate(sorted(nums)):
            if value not in D:
                D[value]=key
        for i in nums:
            the_list.append(D[i])
        return the_list
        