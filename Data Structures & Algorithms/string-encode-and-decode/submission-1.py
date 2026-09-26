class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        result = []
        while i<len(s):
            curr_length = 0
            c = s[i]
            while c != '#':    
                curr_length+=1
                i+=1
                c = s[i]
            str_length = int(s[i-curr_length:i])
            i+=1
            result.append(s[i:i+str_length])
            i+=str_length
        return result
