class Calculator():

    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def aPlusb(self):
        c = self.a + self.b
        return c

    def aMinusb(self):
        c = self.a - self.b
        return c

    def aMumltiplicateb(self):
        c = self.a * self.b
        return c

if __name__ == "__main__":
    c = Calculator(int(input("a=")),int(input("b=")))
    operator = input("operator: ")
    if operator == '+':
        print(c.aPlusb())
    elif operator == '-':
        print(c.aMinusb())
    elif operator == '*':
        print(c.aMumltiplicateb())
    else:
        print("Wrong operation")