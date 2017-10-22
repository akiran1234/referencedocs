# class,object,class variable,instance variable,constructor,inheritance,overiding


a=100                       # module variable

class First:
    x=100                   # class variable

    def __init__(self,l,m): # Constructor by default it is called when ever object is created.
        self.l=l
        self.m=m


    def sum(self,s1,s2):
        self.s3=s1+s2       # self.s3 is instance variable for obj object
        print("Printing from sum method with 2 Args:",self.s3)

    def sum(self):          # This method is overiding the previous method with out inheritance.
        self.s4=self.l+self.m
        print("Printing from sum method with 3 Args:",self.s4)


obj=First(10,20)            # Passing values to constructor.

obj.sum()                   # calling sum method and it refers to last sum() in the class.

print("printing class variable before change:",First.x)
First.x=999
print("printing class variable after change:",First.x)