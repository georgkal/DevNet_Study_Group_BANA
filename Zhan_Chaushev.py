class Calculator():
    def suma(a,b):
        c= a+b
        return c

    def minus(a,b):
        c= a-b
        return c
    def umnojenie(a,b):
        c=a*b
        return c


if __name__ == "__main__":
    a = int(input("Value for a:" ))
    b = int(input("Value for b:"))
    action = input("Choose action: +,-,*: " )
    if action == "+":
        print(a, "+", b, "=", 
                    Calculator.suma(a,b))
    
    elif action == "-":
        print(a, "-", b, "=", 
                    Calculator.minus(a,b))
        
    elif action == "*":
        print(a, "*", b, "=", 
                    Calculator.umnojenie(a,b))
        
    else:
        print ("Illegal action chosen")
    
    
    