class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            length = 1
            if n-1 not in s:
                num = n+1
                while num  in s:
                    length +=1
                    num = num+1
            longest = max(longest,length)

        return longest
