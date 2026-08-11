class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sword = "".join(sorted(word))
            if sword in seen:
                seen[sword].append(word)
            else:
                seen[sword] = [word]
        return list(seen.values())