class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights) -1
        a_max = float('-inf')

        while i < j :
            h = min(heights[i],heights[j])
            l = j-i

            a_max  = max(a_max,h*l)

            if heights[i] > heights[j]:
                j -=1
            
            else: 
                i +=1
        
        return a_max
