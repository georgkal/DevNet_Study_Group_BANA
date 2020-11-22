class Calculator():

    def __init__(self, a, b, action):
        self.a = a
        self.b = b
        self.action = action
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

if __name__ == "__main__":
    calc = Calculator(int(input("Input a: ")), int(input("Input b: ")), input("Input action as \"+\" \"-\" \"*\" or \"/\": "))
    
    if (calc.action == "+"):
        result = calc.add()
    elif (calc.action == "-"):
        result = calc.sub()
    elif (calc.action == "*"):
        result = calc.mul()
    elif (calc.action == "/"):
        result = calc.div()
    else:
        result = "***ERROR***"
    
    print("Result is: " + str(result))