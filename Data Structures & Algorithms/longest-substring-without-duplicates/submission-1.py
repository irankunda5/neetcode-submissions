class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = 0
        cset = set()

        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            m = max(m, r - l + 1)
        
        return m