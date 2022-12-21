class something:
    #constructer
    def __init__(self,f,s):
        self.smthng="something should print"
        self.var1=f
        self.var2=s
    #destructor
    def __del__(self):
        print("destructor called,program ends")
    #methods
    def display(self):
        print(self.smthng)
        
    def product(self):
        p=self.var1*self.var2
        print(p)
obj=something(8,9)

obj.display()


obj.product()

del obj