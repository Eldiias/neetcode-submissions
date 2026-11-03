class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case '+':
                        res = a+b
                    case '-':
                        res = a-b
                    case '*':
                        res = a*b
                    case '/':
                        res = int(a/b)
                stack.append(res)
        return int(stack[-1])