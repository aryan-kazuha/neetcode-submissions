class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1

        max_val = float('-inf')

        while right > left:
            h = min(heights[left],heights[right])
            l = right - left

            water = h*l
            max_val = max(max_val,water)

            if heights[right]>heights[left]:
                left +=1
            
            else:
                right -=1
        return max_val