class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)

        ans = [0]*n
        ans[n-1] = 0
        stack.append(n-1)
        
        for i in range(n-2,-1,-1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if len(stack) == 0:
                ans[i] = 0
            
            else:
                ans[i] = stack[-1] - i
            
            stack.append(i)
        
        return ans