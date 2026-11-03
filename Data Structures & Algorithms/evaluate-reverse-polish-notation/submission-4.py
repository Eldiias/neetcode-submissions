class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cifers = [f"{i}" for i in range(10)]
        sol = 0
        stack = []
        for i in tokens:
            if i[-1] in cifers:
                stack.append(int(i))
            else:
                print(stack)
                print(i)
                q = stack.pop()
                w = stack.pop()
                if i == '+':
                    stack.append(w+q)
                elif i == '-':
                    stack.append(w-q)
                elif i == '*':
                    stack.append(w*q)
                elif i == '/':

                    stack.append(int(w/q))
        return stack[-1]