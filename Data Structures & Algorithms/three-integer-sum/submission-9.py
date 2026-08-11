from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        # We only need to go up to n - 2 because we need 3 elements
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            lo, hi = i + 1, n - 1
            while lo < hi:
                ssum = nums[i] + nums[lo] + nums[hi]
                
                if ssum == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # Skip duplicate values for the left pointer
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    # Skip duplicate values for the right pointer
                    while lo < hi and nums[hi] == nums[hi + 1]: # Note: changed to hi + 1 for clarity
                        hi -= 1
                elif ssum < 0:
                    lo += 1
                else:
                    hi -= 1
                    
        return res
