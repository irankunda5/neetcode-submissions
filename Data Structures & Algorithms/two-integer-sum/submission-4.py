class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Maps the value to its index
        
        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem], i]
            else:
                seen[num] = i          