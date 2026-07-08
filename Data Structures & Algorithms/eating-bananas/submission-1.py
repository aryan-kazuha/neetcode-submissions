class Solution:
    def calc(self,arr,guess):
        hrs = 0
        for a in arr:
            if a%guess == 0:
                hrs += a/guess
            else:
                hrs +=(a//guess) +1
        return hrs
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = 0

        while low<=high:
            mid = (low +high)//2

            if self.calc(piles,mid) > h:
                low = mid +1
            
            else:
                res = mid
                high = mid -1
        return res

