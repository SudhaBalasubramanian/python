class Fibonacci:
    def __init__(self, end):
        self.previous = 0
        self.current = 1
        self.n = 1
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < self.end:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n = self.n + 1
            return result
        else:
            raise StopIteration
        
nums = Fibonacci(5)        
for num in nums:
    print(num)
        
