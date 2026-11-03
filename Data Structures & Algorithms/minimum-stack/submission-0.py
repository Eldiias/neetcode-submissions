class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_ = float('inf')
        self.min_ = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_.append(min(self.min_ + [val]))
        # if self.min_:
        #     self.min_ = min(self.min_, val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]
