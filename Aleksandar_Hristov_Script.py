class Calculator():

    def aPlusb(a,b):
        c = a + b
        return c

    def aMinusb(a,b):
        c = a - b
        return c

    def aMumltiplicateb(a,b):
        c = a * b
        return c

if __name__ == "__main__":
    c = Calculator.aPlusb(int(input("a=")),int(input("b=")))
    print(c)