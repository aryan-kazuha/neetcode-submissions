class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashm = {}

        for x in s:
            hashm[x] = hashm.get(x,0) +1

        for x in t:
            if hashm.get(x,0) == 0:
                return False

            else :
                hashm[x] = hashm.get(x) -1
            
        for val in hashm.values():
            if val != 0:
                return False
        
        return True