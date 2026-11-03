# class MinStack:
# This solution is implemented using 2 stack approach. Results: 3ms, 21.3 MB

#     def __init__(self):
#         self.stack = []
#         self.min_ = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.min_.append(min(self.min_[-1],val) if self.min_ else val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_[-1]

class MinStack:
# This solution is implemented using a single stack. Results: 0ms, 21.3 MB
    def __init__(self):
        self.stack = []
        self.min_ = float('inf')

    def push(self, val: int) -> None:
        if len(self.stack)>0:
            self.stack.append(val-self.min_)
            if val<self.min_:
                self.min_ = val
        else:
            self.stack.append(0)
            self.min_ = val

    def pop(self) -> None:
        k = self.stack.pop()
        if k<0:
            self.min_ -= k 

    def top(self) -> int:
        return self.stack[-1]+self.min_ if self.stack[-1]>0 else self.min_

    def getMin(self) -> int:
        return self.min_
