class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in seen:
                seen[i]+= 1
            else:
                seen[i] = 1
        for n,c in seen.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                

        