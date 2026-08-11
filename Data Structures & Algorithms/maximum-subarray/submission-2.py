class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = -100000
        csum = 0

        for i in range(len(nums)):
            if csum < 0:
                csum = 0
            csum += nums[i]
            msum = max(msum, csum)
        return msum