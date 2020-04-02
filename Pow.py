class Power:
    def __init__(self, a):
        self.a = a
    
    def power(self, n):
        self.s = self.a
        for i in range(n - 1):
            self.a *= self.s

        return self.a

a = Power(2)
print(a.power(10))