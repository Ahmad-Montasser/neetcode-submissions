class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        res,l = 0,0
        count = {}
        for r,c in enumerate(s):
            count[c] = count.get(c,0) + 1
            maxf = max(count[c],maxf)
            while l <= r:
                if r - l - maxf + 1 <= k:
                    res = max(r-l+1,res)
                    break
                else:
                    count[s[l]] -=1
                    l+=1

                


        return res
