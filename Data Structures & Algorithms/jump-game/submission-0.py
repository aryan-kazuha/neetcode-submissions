class Solution:
    def canJump(self, arr: List[int]) -> bool:
        
        reach = 0

        for i in range(len(arr)):

            if reach < i  :
                return False
            
            reach = max(reach,i + arr[i])

            if reach >=len(arr):
                return True
        return True
        
            
