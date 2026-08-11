class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        biggest = -1000
        for i in nums:
            if curr + i < i:
                curr = i
            else:
                curr += i
            biggest = max(biggest , curr)
        return biggest