class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        count = {}
        max_len = 1

        for high in range(len(s)):
            count[s[high]] = count.get(s[high],0) + 1

            cur_len = high - low +1
            
            while cur_len - max(count.values()) > k:
                count[s[low]] -=1
                low +=1
                cur_len -=1
            
            max_len = max(max_len,cur_len)
        
        return max_len

                
