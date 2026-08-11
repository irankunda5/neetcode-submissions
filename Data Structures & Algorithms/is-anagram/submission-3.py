class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        si, ti = {}, {}

        for i in range(len(s)):
            si[s[i]] = 1 + si.get(s[i], 0)
            ti[t[i]] = 1 + ti.get(t[i], 0)
        return si == ti