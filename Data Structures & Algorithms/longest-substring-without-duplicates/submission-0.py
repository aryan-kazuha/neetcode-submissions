class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        high = 0
        low = 0

        max_len = 0

        while high< len(s):
            count[s[high]] = count.get(s[high],0) + 1

            while max(count.values()) > 1:
                count[s[low]] -=1
                low +=1

            max_len= max(max_len,high-low+1)
            high +=1
            

        return max_len
