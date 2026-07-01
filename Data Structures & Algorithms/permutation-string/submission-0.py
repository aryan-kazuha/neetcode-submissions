class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}

        for x in s1:
            count_s1[x] = count_s1.get(x,0) +1

        low = 0
        count_s2 = {}

        for high in range(len(s2)):
            count_s2[s2[high]] = count_s2.get(s2[high],0) +1
            cur_len = high - low +1

            while len(s1) < cur_len:
                count_s2[s2[low]] -= 1

                if count_s2[s2[low]] == 0:
                    del count_s2[s2[low]]
                low +=1
                cur_len -=1

                

            if count_s2 == count_s1:
                return True
        
        return False
