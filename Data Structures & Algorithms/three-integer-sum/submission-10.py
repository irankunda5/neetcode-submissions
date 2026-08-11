class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i+1, n-1

            while lo < hi:
                ssum = nums[i] + nums[lo] + nums[hi]
                if ssum == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1
                    while nums[hi] == nums[hi + 1] and lo < hi:
                        hi -= 1
                elif ssum < 0:
                    lo += 1
                else:
                    hi -= 1
        return res
