class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}
        hash_ = {}

        for x in s:
            freq[x] = freq.get(x,0) +1
        
        for y in t:
            hash_[y] = hash_.get(y,0) + 1

        if freq != hash_ :
            return False
        
        return True
        