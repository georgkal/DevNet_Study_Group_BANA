class Calculate():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def addition(self):
        return self.a + self.b
    def divide(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b

input_a = int(input("Enter first digit: "))
input_b = int(input("Enter seconf digit: "))
input_oper = input("Enter operator + , - or *: ")

if  input_oper == "+":
    add = Calculate(input_a, input_b)
    print(f"Result is: {add.addition()}")
elif input_oper == "-":
    div = Calculate(input_a, input_b)
    print(f"Result is: {div.divide()}")
elif input_oper == "*":
    mlt = Calculate(input_a, input_b)
    print(f"Result is: {mlt.multiply()}")
else:
    print("Wrong operator, try again!")