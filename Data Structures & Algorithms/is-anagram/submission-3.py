class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashm = {}
        hashn = {}

        for x in s:
            hashm[x] = hashm.get(x,0) +1
        for x in t:
            hashn[x] = hashn.get(x,0) +1

        if hashm != hashn :
            return False
        
        return True