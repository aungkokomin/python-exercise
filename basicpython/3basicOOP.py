class Counter:
    def __init__(self, start:int=0):
        self.value = start
    
    def increment(self,by:int=1):
        self.value += by
        return self

c = Counter().increment().increment().increment().increment().increment()
print(c.value)