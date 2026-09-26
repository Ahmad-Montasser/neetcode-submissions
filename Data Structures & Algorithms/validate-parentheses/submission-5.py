class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(',']':'[','}':'{'}
        l = []
        for c in s:
            if not c in valid:
                l.append(c)
            else:
                if l and valid[c] == l[-1]:
                    l.pop()
                else:
                    return False
        if l:
            return False
        else:
            return True