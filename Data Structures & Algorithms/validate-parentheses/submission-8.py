class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cor = {"]":"[", "}":"{", ")":"("}

        if (s[0] in cor.keys()):
            return False
        
        for p in s:
            if p in cor.keys():
                if stack and stack[-1] == cor[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False