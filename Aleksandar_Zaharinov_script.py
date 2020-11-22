class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sbor(a,b):
        c = a + b
        return c

    def razlika(a,b):
        c = a - b
        return c
    
    def umnojenie(a,b):
        c = a * b
        return c

if __name__ == "__main__":
    a=int(input("Plese set a value for a:"))
    b=int(input("Plese set a value for b:"))
results = (Calculator.sbor(a,b),Calculator.razlika(a,b),Calculator.umnojenie(a,b))
print (results)