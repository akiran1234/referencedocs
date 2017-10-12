x=100
y=[10,20,39]

print('This is SampleTest Module')
print('SampleTest Module Values x,y=',x,y)
print('In module_math script name =',__file__)      # Print the module name with absolute path
print('In module_math value of __name__ is:',__name__)      # Print the main script script.

def add(a,b):
    """This is add function in SampleTest module """
    c=a+b
    return c

def sub(a,b):
    """This is subtraction function in Sample Module"""
    c=a-b
    return c

def mul(x1,y1):
    """This is multiplication function in sample module"""
    c=x1*y1
    return c

print('In module_math=',add.__doc__)   # Print the doc string of add function