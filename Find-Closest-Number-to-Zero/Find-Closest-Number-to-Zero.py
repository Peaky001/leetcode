class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        updated_list  =  []
        for i in nums:
            multiplied_value  = (abs(i)-0)
            updated_list.append(multiplied_value)

        min_value = min(updated_list) 
        return min_value if min_value in nums else -min_value

