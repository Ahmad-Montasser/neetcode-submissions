class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for n in nums:
            if n in x:
                return True
            x[n] = 0
        return False    