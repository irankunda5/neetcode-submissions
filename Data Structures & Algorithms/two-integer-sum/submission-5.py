class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if nums[i] in comp:
                return [comp[nums[i]], i]
            else:
                comp[c] = i