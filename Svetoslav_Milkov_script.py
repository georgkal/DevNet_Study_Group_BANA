#!/usr/bin/env python3

class calculator():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        c = self.a + self.b
        return c

    def subtraction(self):
        c = self.a - self.b
        return c

    def multiplication(self):
        c = self.a * self.b
        return c


# if __init__ == "__main__":

operator = input("Chose an operator: ")
a = int(input("Choose a number: "))
b = int(input("Choose a second number: "))

if operator == "+":
    result = calculator(a, b)
    print(result.addition())

elif operator == "-":
    result = calculator(a,b)
    print(result.subtraction())
elif operator == "*":
    result = calculator(a,b)
    print(result.multiplication())

