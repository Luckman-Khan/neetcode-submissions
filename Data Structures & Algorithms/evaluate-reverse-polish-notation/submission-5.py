class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        ops = {
            '+':lambda a,b: a+b,
            '-':lambda a,b: a-b,
            '*':lambda a,b: a*b,
            '/':lambda a,b: int(a/b),
        }

        for ch in tokens:

            if ch not in '+-*/':
                stack.append(ch)

            else:
                num1  = int(stack.pop())
                num2 = int(stack.pop())

                result = ops[ch](num2,num1)
                stack.append(result)

        res = stack.pop()
        return int(res)

