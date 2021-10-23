
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


class s_calc(basic_calc):
    def fact(self):
        a = self.a
        b = self.b
        fact_a = 1
        while a:
            fact_a *= a
            a -= 1
        fact_b = 1
        while b:
            fact_b *= b
            b -= 1
        return s_calc(fact_a, fact_b)

    def pow_y(self, y):
        power_a=1
        power_b=1
        for i in range(y):
            power_a = self.a*self.a
            power_b = self.b*self.b
        return power_a, power_b

    def log(self):
        return math.log(self.a), math.log(self.b)

    def ln(self):
        return self.log()


var_1 = basic_calc(1, 2)
print("----------BasicCalc---------")
print(f"Sum of {var_1}: {var_1.add()}")
print(f"Difference of {var_1}: {var_1.sub()}")
print(f"Division of {var_1}: {var_1.div()}")
print(f"Product of {var_1}: {var_1.mul()}")

var_2 = s_calc(3, 4)
print("----------BasicCalc---------")
print(f"Fact of {var_2}: {var_2.fact()}")
print(f"Power of {var_2} to {3}: {var_2.pow_y(3)}")
print(f"Log of {var_2}: {var_2.log()}")
print(f"Ln of {var_2}: {var_2.ln()}")
