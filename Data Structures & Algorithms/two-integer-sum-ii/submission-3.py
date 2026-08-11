class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            rem = numbers[r] + numbers[l]
            if rem < target:
                l += 1
            elif rem > target:
                r -= 1
            elif rem == target:
                return [l+1, r+1]
            