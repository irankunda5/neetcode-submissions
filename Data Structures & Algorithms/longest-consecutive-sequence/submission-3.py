class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in ss:
                length = 0
                while (n+length) in ss:
                    length += 1
                longest = max(length, longest)
            
        return longest
