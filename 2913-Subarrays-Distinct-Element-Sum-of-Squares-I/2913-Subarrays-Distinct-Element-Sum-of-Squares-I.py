class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        subarrays = []
        set_values = []

        n = len(nums)

        for start in range(n):
            for end in range(start + 1, n + 1):
                subarray = nums[start:end]
                subarrays.append(subarray)
            
        for i in subarrays:
            set_values.append(len(set(i)))
        return sum(i**2 for i in set_values)