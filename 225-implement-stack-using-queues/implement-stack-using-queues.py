from collections import deque
class MyStack:

    def __init__(self):
        self.iteams =deque()

    def push(self, x: int) -> None:
       self.iteams.append(x)
       for _ in range(len(self.iteams)-1):
        self.iteams.append(self.iteams.popleft())

    def pop(self) -> int:
        if len(self.iteams)!=0:
            return self.iteams.popleft()

    def top(self) -> int:
        if len(self.iteams)!=0:
            return self.iteams[0]
            

    def empty(self) -> bool:
        if len(self.iteams)!=0:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()