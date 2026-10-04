class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_mul = 1
        r_mul = 1
        l_arr = [1]*n
        r_arr = [1]*n
        for i in range(len(nums)):
            j = -i-1
            l_arr[i] = l_mul
            r_arr[j] = r_mul
            l_mul *= nums[i]
            r_mul *= nums[j]

        return [l*r for l,r in zip(l_arr, r_arr)]