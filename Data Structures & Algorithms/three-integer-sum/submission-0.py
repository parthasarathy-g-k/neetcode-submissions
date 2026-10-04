class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis1 = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j = i+1
            k = len(nums) - 1
            target = -nums[i]
            
            while j<k:
                score = nums[j] + nums[k]
                if score < target:
                    j = j+1
                elif score > target:
                    k = k-1
                else:
                    lis1.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate second elements
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third elements
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return lis1    
