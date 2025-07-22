class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            char = s[i]
            if char in mapping.values():
                stk.append(char)
            else:
                if stk and char in mapping and stk[-1] == mapping[char]:
                    stk.pop()
                else:
                    return False
        if stk == []:
            return True
        else:
            return False