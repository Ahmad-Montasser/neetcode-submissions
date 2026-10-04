class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        valid = {}
        result = set()
        for i,n in enumerate(nums):
            valid[0-n] = i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = nums[i] + nums[j]
                if s in valid and i != valid[s] and j != valid[s]:
                    res = [nums[i], nums[j],0-s]
                    res.sort()
                    result.add(tuple(res))
        
        return [list(i) for i in result]