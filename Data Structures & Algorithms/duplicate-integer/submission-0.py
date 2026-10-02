class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isTrue = len(nums) > len(set(nums))
        return isTrue