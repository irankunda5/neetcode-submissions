class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum, csum = nums[0], 0

        for i in range(len(nums)):
            if csum < 0:
                csum = 0
            csum += nums[i]
            msum = max(csum, msum)
        return msum