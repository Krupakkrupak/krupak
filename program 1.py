class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b == 0:
                return "Cannot divide by zero"
            return self.a / self.b
        else:
            return "Invalid operation"


# Example
c = Calculator(10, 5, "add")
print(c.calculate())
