#!/usr/bin/python3

class Calculator:

    def __init__ (self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        print(self.a + self.b)

    def substract(self):
        print(self.a - self.b)
    
    def multiply(self):
        print(self.a * self.b)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = input("Enter the operation: ")

calculate = Calculator(x, y)

if z == '*':
    result = calculate.multiply()
elif z == '+':
    result = calculate.add()
elif z == '-':
    result = Calculator.substract()
else:
    result = "Invalid action."

print(result)




