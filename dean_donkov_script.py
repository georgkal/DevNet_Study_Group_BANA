#!/usr/bin/python3

class Calculator:

    def __init__ (self, a, b):
        self.a = a
        self.b = b
    
    def add(a, b):
        print(a + b)

    def substract(a, b):
        print(b - a)
    
    def multiply(a, b):
        print(a * b)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = input("Enter the operation: ")

if z == '*':
    result = Calculator.multiply(x, y)  
elif z == '+':
    result = Calculator.add(x, y)
elif z == '-':
    result = Calculator.substract(x, y)
else:
    result = "Invalid action."

print(result)




