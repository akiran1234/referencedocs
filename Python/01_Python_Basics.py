#####################################################################################################################
# Identifiers are the names given to entities like  Variables, functions and classes ..
# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# Names like myClass, var_1 and print_this_to_screen, all are valid example.
# An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
# Keywords cannot be used as identifiers.
# We cannot use special symbols like !, @, #, $, % etc. in our identifier.
# https://www.programiz.com/python-programming/keywords-identifier -- Reference
# Python Naming Convention --- http://visualgit.readthedocs.io/en/latest/pages/naming_convention.html#general


count = 10
print("Printing the value of count", count)

# Literal can be defined as data that is given in a variable/constant. Here 10 is the literal to variable count.

#####################################################################################################################
# Commenting a line in a Python can be done by placing "#" before the statement
# Indentation represents no braces {} to indicate block of code
# Quotations in Python
# Python accepts single ('), double (") and triple (''' or """) quotes
# If quote starts with single/double/triple it should end with single/double/triple.

print('This quote starts and ends with single quote')
print("This quote starts and ends with double quote")
print('''This quote starts and ends with triple quotes''')

#####################################################################################################################
# A statement can be divided into multi line statements by placing back slash \

print("This is multi line \
statement")

print(1+2+\
      3)

#####################################################################################################################
print("Semicolon (;) at the end of the statement in Python is optional");
print("Multiple statements can be executed in a single line by separating with ;")

print(1+2); print(5+6);print("Printing multiple statements in a single line by placing ;")

#####################################################################################################################
# Reading data from standard input (keyboard) and display on standard output using print() function.
# print() is a function belongs to builtins module.
# Reading data using two functions input() and raw_input().
# input(): Interprets and evaluates the input which means that if user enters integer,an integer will be returned,if user enters string,string is returned.
# raw_input(): takes exactly what user typed and passes it back as string .It doesn't interprets the user input.
# Even an integer value of 10 is entered or a list is entered its type will be of string only.

str1=input()                                             # Execute in a separate script for better understanding; input= read in linux.
print("Printing from the standard input function:",str1) # Printing standard output on screen


# str2=raw_input()                        # Execute in a separate script for better understanding
# print("Printing from the standard input function:",str2)

#####################################################################################################################
# Command line arguments pending

########### Python Architecture ############################
# Python is an interpreted language it will read each line and execute.
# Each script in python is a module.
# Module will have variables, functions and classes.
# Modules can be imported from the library path and it's attributes like variables, functions and classes can be utilized.
help('modules')        # run this help function - will list all the available modules in the library.
help('modulename')     # Ex: help('re')--> will give the list of functions available in the module.
# Python has many builtin functions to know a particular function belongs to which module can be queried.
print.__module__       # This will query print() method belongs to which module

dir()              	   # is a function to get the list of attributes/functions used in the module.
dir(object)            # s='string' s is object of string class. To list the methods of class string: dir(s).
id(object)             # This will return the address of object. a=10; type(a)- This will return the address of object a.

# modules path         # C:\Program Files\Python36\Lib in windows.
# module index         # https://docs.python.org/3/py-modindex.html
