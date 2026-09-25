class DynamicArray:
    l = []
    size = 0
    def __init__(self, capacity: int):
        self.l = []
        self.size = capacity
    def get(self, i: int) -> int:
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        self.l[i] = n

    def pushback(self, n: int) -> None:
        if len(self.l) >= self.size:
            self.resize()
        self.l.append(n)
        
    def popback(self) -> int:
        return self.l.pop(len(self.l)-1)
    def resize(self) -> None:
        self.size *=2
    def getSize(self) -> int:
        return len(self.l)
    
    def getCapacity(self) -> int:
        return self.size

    