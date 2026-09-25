class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""
        for n in s:
            if not n.isalnum():
                continue
            alpha += n.lower()
        l,r = 0,len(alpha)-1
        while l <r:
            if alpha[l] != alpha[r]:
                return False
            l +=1
            r -=1
        return True
