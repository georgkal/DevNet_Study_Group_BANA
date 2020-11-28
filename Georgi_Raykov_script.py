class Calculate:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def add(self):
        c= self.a + self.b
        return(c)
    def mult(self):
        c = self.a * self.b
        return(c)
    def sub(self):
        c = self.a - self.b
        return(c)
if __name__ == "__main__":
    a = int(input("Please set a value for A: "))
    b = int(input("Please set value for B: "))
    action = input("Please select action using '+''-' or '*' :")
    if action == '+':
        added = Calculate(a,b)
        print(added.add())
    elif action == '-':
        subst = Calculate(a,b)
        print(subst.sub())
    elif action == '*':
        multip = Calculate(a,b)
        print(multip.mult())
    else:
        print("Invalid action was selected")