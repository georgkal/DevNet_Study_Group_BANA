#!/usr/bin/env python3
#Added by Ivaylo Petrov

class Calculate:
    
    def plus(a,b):
        return a + b
    
    def minus(a,b):
        return a - b

    def po(a,b):
        return a * b

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(type(a))
    print(type(b))


    while ( TypeError != int:
        a = input("Enter a: ")
        break

    while (type(b) != int):
        b = int(input("Enter b: "))
        break
    
    opcia = str(input("Input Action `+`,`-` or `*` :"))
    
    if (opcia == "+"):
        result = int(Calculate.plus(a,b))
        print(result)
    elif (opcia == "-"):
        result = int(Calculate.minus(a,b))
        print(result)
    elif (opcia == "*"):
        result = int(Calculate.po(a,b))
        print(result)
    else:
        print("Action not allowed!!!")