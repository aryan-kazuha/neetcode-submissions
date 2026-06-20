class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ind = {}

        for  idx,val in enumerate(nums):
            ind[val] = idx

        for i,num in enumerate(nums):
            need = target - num

            if need in ind and i != ind[need]:
                return [i,ind[need]]
            
        
        