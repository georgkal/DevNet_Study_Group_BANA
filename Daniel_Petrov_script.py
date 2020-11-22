# usr/bin/env python3 

class Calculator():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum (self, a, b):
        return self.a + self.b

    def sub (self, a, b):
        return self.a + self.b

    def mul (self, a, b):
        return self.a * self.b

if __name__ == "__main__":

    # Get values for a and b
    a = int(input("Please input a value for a: "))
    b = int(input("Please input a value for b: "))

    # Define an object from class Calculator
    test_object = Calculator(a, b)

    operation = input("What operation would you like to do? \n1. Sum a and b \n2. Substract b from a \n3. Multiply a and b \n (Drum rolls) And your choice is... :")

    print (operation)

    if int(operation) == 1:
        print ("The sum of a and b is: %d" %test_object.sum(a,b))
    elif int(operation) == 2:
        print ("The result is: %d" %test_object.sub(a,b))
    elif int(operation) == 3:
        print ("a and b multiplied gives us: %d" %test_object.mul(a,b))
    else:
        print ("Please select a valid option!")


