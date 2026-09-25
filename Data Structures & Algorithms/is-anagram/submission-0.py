class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0]*26
        for n in range(len(s)):
            n1 = ord(s[n])- 97
            n2 = ord(t[n])- 97
            count[n1] += 1
            count[n2] -= 1
        for n in count:
            if n != 0:
                return False
        return True 