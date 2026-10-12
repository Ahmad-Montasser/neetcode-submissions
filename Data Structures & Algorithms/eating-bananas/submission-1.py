class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minEatingSpeed = max(piles)
        # print(f"l => {l}")
        # print(f"r => {r}")
        while l <= r:
            currSpeed = ((l + r) // 2)
            valid = True
            # print(f"currSpeed => {currSpeed}")
            currHours = 0
            for pile in piles:
                currBananas = pile 
                currHours += math.ceil(currBananas/currSpeed)
                
                if currHours > h:
                    valid = False
                    break
            # print(f"currHours => {currHours}")    

            if valid:
                minEatingSpeed = min(currSpeed,minEatingSpeed)
                r = ((l + r) // 2) - 1
            else:
                l = ((l + r) // 2) + 1
            # print(f"minEatingSpeed => {minEatingSpeed}")
        return minEatingSpeed
            
