class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        new_list = []
        for i in range(len(nums)):
           sum += nums[i]
           new_list.append(sum)
        return new_list
        
        my_list = list(map(int,input().split()))
        result = runningSum(my_list)
        print(result)