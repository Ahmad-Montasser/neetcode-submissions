class MinStack:

    def __init__(self):
        self.stack = []    
        self.mini = None
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.mini != None:
            self.mini = min(self.mini,val)
        else:
            self.mini = val 

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.mini = None
            return
        
        self.mini = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini
