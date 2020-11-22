class Calculation():

    def collection(a,b):
        c = a+b
        return(c)

    def substraction(a,b):
        c = a-b
        return(c)
    
    def multiplication(a,b):
        c = a*b
        return(c)

if __name__ == "__main__":
    a = int (input("Put value for a: "))
    b = int (input("Put value for b: "))
    action = (input("Select action by using '+' '*' or '-'"))

    if action == "+":
        collection = Calculation.collection(a,b)
        result = Calculation.collection(a,b)
    elif action == "*":
        collection = Calculation.multiplication(a,b)
        result = Calculation.multiplication(a,b)
    elif action == "-":
        collection = Calculation.substraction(a,b)
        result = Calculation.substraction(a,b)
    print(result)
    