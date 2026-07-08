class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        arr = [item for row in matrix for item in row]

        low = 0
        high = len(arr) -1

        while low <= high:
            mid = (low + high)//2

            if arr[mid] == target:
                return True
            
            elif arr[mid] > target:
                high = mid -1
            else:
                low = mid +1
        
        return False