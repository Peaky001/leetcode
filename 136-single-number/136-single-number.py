class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_dict = collections.Counter(nums)
        for i in new_dict:
            if new_dict[i] == 1:
                return i 