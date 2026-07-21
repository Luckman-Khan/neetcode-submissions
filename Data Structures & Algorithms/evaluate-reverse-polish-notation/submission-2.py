import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        ops = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.truediv,
        }

        for ch in tokens:
            if ch not in '+-*/':
                self.stack.append(ch)
            else:
                o1 = int(self.stack.pop())
                o2 = int(self.stack.pop())

                result = ops[ch](o2,o1)
                self.stack.append(result)
   
        res = self.stack.pop()
       
        return int(res)
            