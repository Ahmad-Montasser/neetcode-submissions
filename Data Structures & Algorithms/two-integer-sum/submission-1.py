class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = {}
        for i,n in enumerate(nums):
            missing = target - n
            if missing in kv:
                return [kv[missing],i]
            kv[n] = i