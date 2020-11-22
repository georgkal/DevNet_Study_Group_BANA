class Cal: 

    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def summary(self):
        return self.a + self.b

    def subst(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

if __name__=="__main__": 

    a=int(input("GIve value for a: "))
    b=int(input("Give value for b: "))
    
    result1 = Cal(a,b).summary() 
    result2 = Cal(a,b).subst()
    result3 = Cal(a,b).multi()

print(f'Sum is {result1} , subtraction is {result2} and multiplication is {result3}')
