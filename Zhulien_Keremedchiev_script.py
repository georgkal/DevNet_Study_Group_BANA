#!/usr/bin/env python3

class Calculator:
    def sybirane(a,b):
        c = a + b
        return(c)
    
    def izvajdane(a,b):
        c = a - b 
        return(c)

    def umnojenie(a,b):
        c = a * b 
        return(c)
    
    def delenie(a,b):
        c = a / b
        return(c)

if __name__ == "__main__":

    a=int(input("Molq vyvedete stoinost za A: "))
    b=int(input("Molq vyvedete stoinost za B: "))
    action = input("Kakvo shte gi pravim? '+' '-' '*' ili '/' :")
    if action == "+":
        sybirane = Calculator.sybirane(a,b)
        print(sybirane)
    elif action == "-":
        izvajdane = Calculator.izvajdane(a,b)
        print(izvajdane)
    elif action == "*":
        umnojenie = Calculator.umnojenie(a,b)
        print(umnojenie)
    elif action == "/":
        delenie = Calculator.delenie(a,b)
        print(delenie)

        