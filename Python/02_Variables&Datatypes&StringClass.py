#####################################################################################################################
# A variable is a location with address in memory used to store some value (data)
# In python we "don't need" to declare a variable before using it.
# One Important feature in python is no need of declaring a data type, interpreter will dynamically identify and assigns its datatype
# In python declaring only variable is not allowed, it has to be declared and assigned with value as shown below.
# Each data type is a class in Python and the declared variable is an object which corresponds to it's class.

# age           # I have declared age variable with out assigning a value which is not valid.
age=30          # Number Variable  - An integer object with value 30 is created for int class.
price=45.456    # Float Variable   - An float object with value 45.456  is created for float class.
name="Python"   # String Variable  - An string object with value "Python" is created for str class (String class).
val=345j        # Complex Variable - An complex object with value 345j is created for complex class.


# Python handles implicit datatype conversion.
a=50            # Now python defines 'a' as int datatype.
a=a+897.457     # Now python implicitly converts 'a' to float datatype.


# In interactive python shell, we can print the values of variables by typing variable name at prompt but in the script level it should be with print statement
print("Printing age, price and name values:",age,price,name)  # Printing the values of assigned variables in script level using print statement


# Assigning  of variables in Python in different ways.
# Single Assignment
x=10            # An integer object 'x' of type 'int class' with value 10
print("Printing x value",x)

# Multiple Assignment
y=z=k=20        # y,z,k this three integer objects are referenced with same address location value=20
print("Printing y,z,k with same reference value",y,z,k)

a, b, c = 10, "Linux", 100.55678
print("Printing a,b,c values:",a,b,c)

# Swamping of variables

x1=100; y1=200
print("Printing x1,y1 values:",x1,y1,'\n')
x1,y1=y1,x1
print("Printing x1,y1 values:",x1,y1,'\n')

# "del" variable is used to delete the assigned values of variables.The variables should be from it's current tracking session.

var1=var2=var3=10
del var1,var2         # Here var1 is deleted but not the assigned  value.
# print(var1)         # if we try to print var1 we get error -name var1 not defined
print("Printing the value of var3:",var3)

#####################################################################################################################
# Data types in Python
# Mutable means changeable and immutable means not changeable
# Sequence is the generic term for an ordered set of values.
# len(),min(),max() are builtin functions which belongs to builtin module and can be applied on sequence datatype objects.

# 1. Numeric data types     # int, long(deprecated), float, complex
# 2. String Data type       # Immutable sequence data type, stores sequence of characters.
# 3. List Data type  []     # Mutable   sequence data type, where we can update,delete,remove the values of list object.
# 4. Tuple Data type ()     # Immutable sequence data type, where we cannot update delete and remove the values of tuple object.
# 5. Set Data type   {}     # A set is an unordered collection i.e no indexing and  with no duplicate elements.
# 6. Dictionary Data type   # Which holds key value data elements.

#####################################################################################################################
# 1. Number Data Types

# int     --> a=10, b=-20
# long    --> a=1238976L, b= -234567L # L represents long data type and denoting with L is deprecated from the latest version.
# float   --> a=105.456, b=25.456, c= -345.456
# complex --> a=35j, b= -56j, d=34+5j; This complex data type is used in scientific programming.

# Each data type represents a class.
# From above int, long, float, complex are classes and declared variables are objects.
# type(obj) - is used to find type of class

type1=10
type2=123454578999943339993489377777777777777777777777777777777777999999999999999999999999999999999999999999999999999999999999999999999999999999
type3=20.56
type4=345j
type5="Python"
print("printing the class/type of variable type1",type(type2))
print("printing the class/type of variable type1",type(type3))
print("printing the class/type of variable type1",type(type4))
print("printing the class/type of variable type1",type(type1))
print("printing the class/type of variable type1",type(type5))

print("**********************")
#####################################################################################################################
# 2. String Data types (Immutable)

# Strings in Python are identified as a continuous  set of characters represented in quotation marks.
# Python allows for either pairs of single or double quotes.
# Subsets of strings can be accessed  using the slice operator ([ ] and [:] ) and indexing.
# Index of the string starts with 0 hence ends with length of string-1 (n-1). Accessing from end of the string starts with -1,-2 and so on.
# The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator.
# Updating & Deleting  the string object is valid but updating & deleting the string indexing characters in in valid.


str1 = 'kiran kumar'
print("Printing the value of str1:",str1)
print("Printing string length:",len(str1))  # Length=11, Here len() function belongs to builtin module but not related to string class.
print("Printing the 1st char:",str1[0])     # Printing the first character using python slice operator [] by specifying the index number.
print("Printing the 2nd char:",str1[1])     # Printing the second character
print("Printing the last char:",str1[10])   # Index starts with 0 and ends with 10
print("Printing from last 1st char with out knowing the length of string:", str1[-1])  # Useful to print the last character with out knowing the length of string.
print("Printing from last 2nd char with out knowing the length of string:", str1[-2])  # Useful to print the last character with out knowing the length of string.

print("Printing using range slicing:",str1[1:4])   # 1 means start and include this index position, 4 means extract till and exclude this index position in extraction of substring.
print("slicing with out start of index:",str1[:4]) # By default it will start index from 0 and extracts to 3 char by excluding 4th char.
print("slicing with out end of index:",str1[2:])   # It will start extracting from index 2 (Including)  to till end of the string.

print(str1[:-3])      # start index 0 and end index -3 (excluded)
print(str1[-5:-2])    # start index -5 (included) and end index -2 (excluded)
# print(str1[-5:-6])  # This will not work since this cannot traverse in revere direction. End index is greater than start index
print(str1[2:100])    # Start index 2 end index 100 excluded so till 99 it has to print. 99 is out of boundary but it is handled.
# str1[2]='a'         # This is in valid for string objects, updating and deleting is in valid.
# Reference --> https://docs.python.org/2/tutorial/introduction.html

str1="hellopython"    # str1 is overwritten which is valid
print("Printing overwritten string object:",str1)

print("**********************")
#####################################################################################################################
# String operators
# Most of the below operators are in common and applicable to data sequence objects (string,list,tuple) to retrieve the data.

# +       --> Concatenation operator, which will concat two or more string objects.
# *       --> Repetition operator,    which will create new string by concatenating multiple copies of the same string.
# []      --> Slice operator,         Will give the character from the given index.
# [:]     --> Range Slice operator,   will give the character's from the given range.
# in      --> Membership operator,    Returns true if character exists in the given string.
# not in  --> Membership operator,    Returns true if character doesn't exists in the given string.
# % or {} --> Format specifier,       in old version using % and new version using {}.

s1="Hello"
s2="Python"

print("Concatenating s1 and s2:",s1+s2)
print("Concatenating s1 and s2 with space:",s1+" "+s2)
print("Concatenating s1 and s2 with Linux:",s1+" "+s2+"Linux")

print("Repeating the string:",s1*3)                       # String s1 will be printed thrice
print("Repeating the string:",s1+s2*3)                    # String s1 concatenated with thrice s2
print("Repeating the string:",(s1+s2)*3)                  # String s1 and s2 concatenated and printed thrice.

print("Slice operator usage:",s1[0])                      # Printing first character using slice operator
print("Range Slice operator usage:",s1[2:4])              # Printing the character using range slice operator

print("Membership operator usage:", "l" in "apple")       # checking the char 'l' is part of string 'apple'
print("Membership operator usage:", "pl" in "apple")      # checking the char 'pl' is part of string 'apple'

print("Membership operator usage:", "k" not in "apple")   # checking the char 'k' is part of string 'apple'
print("Membership operator usage:", "ak" not in "apple")  # checking the char 'pl' is part of string 'apple'

print("%s asked %d questions on stackoverflow.com" % ("Alex", 99))        # This is the old method of format specifier in print statement.
print("{0} asked {1} questions on stackoverflow.com".format("Alex", 99))  # This is the new method of format specifier in print statement.
print("Linux paid ${0} for purchasing {1} units of {2}".format(550.5,100,"Laptops")) # ${0}=550.5, ${1}=100, ${2}=Laptops

print("**********************")
#####################################################################################################################
# Sting Methods
# String class have few built in methods which can be accessed using string objects.
# len(),min(),max() are builtin functions which belongs to builtin module and can be applied on sequence datatype objects.
# Few important string methods: s3.count('substr'); s3.index('char'), s3.lower(), s3.upper(),s3.isalpha()
# str(list); list(s) : This is conversion function converts list to string; string to list

s3="string methods"

print(s3.lower())    # Prints in lower case
print(s3.upper())    # Prints in upper case
print(s3.__len__())  # Prints length of the string.
print(len(s3))       # This is a builtin function belongs to  __builtin__ module of python hence this function is not accessed with s3 object.
dir(s3)              # This will list all the methods of s3 objects.


# list of methods of string class                       -->  https://www.tutorialspoint.com/python/python_strings.htm
# list of functions which belongs to __builtin__ module -->  https://docs.python.org/3/library/functions.html

#####################################################################################################################















