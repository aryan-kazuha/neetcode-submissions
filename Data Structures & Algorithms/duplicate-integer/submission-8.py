class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = {}

        if len(nums) == 0:
            return False

        for ele in nums:
            hashm[ele] = hashm.get(ele,0) +1 
        
        if max(hashm.values())>1:
            return True
        
        return False
            