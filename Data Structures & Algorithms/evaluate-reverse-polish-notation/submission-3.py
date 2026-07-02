class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = '+-*/'
        stack = []
        for ele in tokens:
            if ele not in ops:
                stack.append(int(ele))

            else:
                b = stack.pop()
                a = stack.pop()

                if ele == '+':
                    stack.append(a+b)
                elif ele == '-':
                    stack.append(a-b)
                elif ele == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        
        return stack[-1]
        
