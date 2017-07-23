#################################################################################################################
# Function is a  block of code to perform specific task. Write once and use multiple times.
# Function are two types 1. Builtin functions 2. User Defined Functions
# Large programs will be sub divided into smaller chunks of code henceforth the programs will be more readable.
# Function will have function name, arguments,indention,block of statements and return type.
# help('modules') # run this help function - will list all the available modules in the library.
# dir() is a builtin function to get the list of attributes/functions used in the module. Ex: dir(math)
#################################################################################################################

# function with out parameters.

def first():                                           # Function definition start with keyword  "def" followed by "fun name" and indentation (:)
    """This is first function with out return stmt"""  # This is a doc string which tells the functionality of the function.
    print( "Hello this is usage of function!!" )       # Here starts the function body followed by return statement and it is optional.


print("Calling & Checking return type:",first())       # I am calling function first() whose return type is none.
print(first.__doc__)                                   # Usage of doc string. ** doc string is only for functions but not for class methods.**

print("1 **********************")
#################################################################################################################
# functions with arguments are divided into 4 categories
# 1.Default arguments  2. Required arguments   3.Keyword arguments    4.Keyword arguments

def defarg(age, name='kiran',):                  # "Non default arguments" should be always placed first and followed by "Default arguments"
    """Default argument functionality"""
    x=name;y=age+10;
    print("Name and age:",x,y,sep=',')
    return y

print(defarg(28))                                # Function not passing name argument the defined default will be taken
print(defarg(28,'Python'))                       # Calling function arguments should be in same order of function definition

print("2 **********************")
#################################################################################################################
# 2. Required Arguments
# Required arguments are the mandatory arguments of a function. These argument values must be passed in correct number and order during function call.
# def sum(name,age): --> Defining function
#   sum('Linux',20) -> Calling function with mandatory arguments (2) and matching data types (string,int).
#################################################################################################################
# 3. Key word Arguments
# In key word arguments, arguments will be called with keyword and  the arguments can be in any order.
#  def sum(name,age,price):
# sum(name='Unix',age=27,price=230.45)      # Calling the arguments with names assigned with values.
# sum(price=230.45,name='Unix',age=27,)     # Order of the arguments is not same with function definition.
#################################################################################################################
# 4. Variable length Arguments
# If the no of arguments that will be passed to a function is not sure then the argument should be declared as Variable length argument.

def vararg(name,*arg):
    for x in arg:
        print('Printing arguments name is:{0} and variable argument:{1}'.format(name,x))


vararg('python',10,20,30)           # First argument ('python') will assigned to 'name' rest will be variable arguments (10,20,30).
vararg(999999,12.34,'Hello',34)     # Name=999999, *args=12.34,'Hello',34

#################################################################################################################
# Call by Value and Call by reference.






