class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for x in nums:
            hash[x] = hash.get(x,0) + 1

        if not hash:
            return False

        val = max(hash.values())
        if val > 1:
            return True
        
        return False
        