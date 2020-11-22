
class Calc():
    def __init__(self,a,B):
        self.a = a
        self.B = B
        
    def multi(self):
        return(self.a * self.B)

    def minu(self):
        return(self.a - self.B)

    def sum(self):
        return(self.a + self.B)
        
a = int(input("Put value for A:"))
B = int(input("Put value for B:"))
Action = input("Put your action (sum, minu or multi): ")

if Action == "multi":
    result = Calc(a ,B)
    print(result.multi()) 
elif Action == "minu":
    result = Calc(a ,B)
    print(result.minu())
elif Action == "sum":
    result = Calc(a ,B)
    print(result.sum())
else: 
    print("n/a")