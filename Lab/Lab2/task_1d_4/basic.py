
class basic_calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return (f"({self.a}, {self.b})")

    def add(self):
        return self.a + self.b

    def div(self):
        return self.a / self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b
