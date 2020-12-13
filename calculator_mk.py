class Calculate:

    def collection(a,b):
        c = a + b
        return(c)
    def substraction(a,b):
         c = a - b
        return(c)
    def multiplication(a,b):
        c = a * b
        return(c)
if __name__ == '__main__':
a=int(input("Please set a value for A: "))
b=int(input("Please se a value for B: "))
action = input("Please select action using '+' '-' or '*' :")
    if action == '+':
        collection = Calculate(a,b)
        print(collection.collection())
    elif action == '_':
        substraction = Calculate(a,b)
        print(substraction.substraction())
    elif action == '*':
        multiplication = Calculate(a,b)
        print(multiplication.multiplication())
    else:
        print("Invalid action was selected : -->3 {}.Exiting".format(action))


