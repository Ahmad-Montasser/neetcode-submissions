class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        targets = {}
        results = set()
        for i,n in enumerate(nums):
            targets[0-n] = i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) in targets and i != targets[nums[i]+nums[j]]and j != targets[nums[i]+nums[j]]:
                    curr = tuple(sorted([nums[i],nums[j],0-nums[i]-nums[j]]))
                    if curr in results:
                        continue
                    results.add(curr)
                    result.append(curr)
        return result

