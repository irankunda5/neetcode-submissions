class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1, r+1]
            elif summ < target:
                if numbers[l] == numbers[l+1]:
                    continue
                else:
                    l += 1
            else:
                if numbers[r] == numbers[r-1]:
                    continue
                else:
                    r -= 1