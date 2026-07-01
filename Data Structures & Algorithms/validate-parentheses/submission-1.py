class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {']':'[',')':'(','}':'{'}

        stack = []

        for x in s:
            if x in mapping:
                if stack and stack[-1] == mapping[x]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(x)

        return len(stack) == 0

