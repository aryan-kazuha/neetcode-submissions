class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i,x in enumerate(nums):
            h[x] =  i
        
        for i in range(len(nums)):
            need = target - nums[i]

            if need in h and h[need] != i:
                return [i,h[need]]