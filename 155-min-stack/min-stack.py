class MinStack:

    def __init__(self):
        self.iteams=[]

    def push(self, value: int) -> None:
        if len(self.iteams)==0:
            self.iteams.append([value,value])
        else:
            mini=min(self.iteams[-1][1],value)
            self.iteams.append([value,mini])

    def pop(self) -> None:
        if self.iteams:
            self.iteams.pop()

    def top(self) -> int:
        if len(self.iteams)==0:
            return 0
        return self.iteams[-1][0]

    def getMin(self) -> int:
        if len(self.iteams)==0:
            return 0
        return self.iteams[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()