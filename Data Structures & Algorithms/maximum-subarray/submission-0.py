class Solution:
    def maxSubArray(self, a: List[int]) -> int:

        best_max,res = a[0],a[0]
        
        for i in a[1:]:

            best_max = max(best_max + i,i)
            res = max(res,best_max)
        
        return res