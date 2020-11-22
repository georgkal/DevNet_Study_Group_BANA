import operator
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class Calculator():

    def __init__(self, a, b, action):
        self.a = a
        self.b = b
        self.action = action
    
    def calculate(self):
        return ops[self.action](self.a, self.b)

if __name__ == "__main__":
    try:
        calc = Calculator(int(input("Input a: ")), int(input("Input b: ")), input("Input action as \"+\" \"-\" \"*\" or \"/\": "))
    except:
        print("Invalid input!")
        exit()
    
    if (calc.action != "+" and calc.action != "-" and calc.action != "*" and calc.action != "/"):
        result = "Invalid action!"
    else:
        result = calc.calculate()
    
    print("Result is: " + str(result))