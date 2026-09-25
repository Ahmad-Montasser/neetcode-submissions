class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            count = [0] * 26
            for n in s:
                count[ord(n) - 97] += 1
            key = "".join(f"X{str(n)}" for n in count)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        result = []
        for x in anagrams:
            result.append(anagrams[x])
        return result