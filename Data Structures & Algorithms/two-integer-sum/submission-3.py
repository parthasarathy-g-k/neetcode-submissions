class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {x:i for i,x in enumerate(nums)}

        for i in range(len(nums)):
            j = target - nums[i]
            if j in dic and dic[j]!=i:
                return [i, dic[j]]



        
            