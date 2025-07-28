class MinStack:

    def __init__(self):
        self.obj = []
        self.objmin = []

    def push(self, val: int) -> None:
        self.obj.append(val)
        if not self.objmin or val <= self.objmin[-1]:
            self.objmin.append(val)

    def pop(self) -> None:
        x = self.obj.pop()
        if x == self.objmin[-1]:
            self.objmin.pop()

    def top(self) -> int:
        return self.obj[-1]

    def getMin(self) -> int:
        return self.objmin[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()