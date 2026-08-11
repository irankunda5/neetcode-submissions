class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            cmp = target - num
            if cmp in seen:
                return [seen[cmp]+1, i+1]
            seen[num] = i