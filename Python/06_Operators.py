#################################################################################################################
# Operators and it's precedence
# Operations on operand (Variables) will be performed using operators.
# Each operator is a function and belongs to operator module.
# Refer Bottom of the page for operator functions --> https://docs.python.org/2/library/operator.html

# 1. Arithmetic operators                          ( +, -, *, /, %, **, // )
# 2. Relational operators / Comparision operators  ( ==, !=, <, >, <=, >= )
# 3. Assignment Operators                          ( =, +=, -=, *=, /=, %=, **=, //= )
# 4. Logical Operators                             ( and, or, not)
# 5. Bitwise Operators
# 6. Membership Operators                          (In, Not In)
# 7. Identity Operators (Python)                   (is, is not)
# 8. Operators Precedence  # PEMDAS (Parenthesis, Exponent, Multiplication, Division, Addition, Subtract) is the acronym to remember precedence of operators.

#################################################################################################################
# 1. Arithmetic Operators
a = 7;
b = 3;

print( a // b )  # Floor Division Operator, which results "Quotient"
print( a % b )  # Modulus Operation which results "Reminder".
print( a ** b )  # Exponent Operation which results 7^3=7*7*7.
print( a * b )  # This is multiplication operation.
print( a + b )
print( a - b )

print( "**********************" )
#################################################################################################################
# 2. Relational operators
a = 7;
b = 3;

print( a == b )  # Floor Division Operator, which results "Quotient"
print( a != b )  # Modulus Operation which results "Reminder".
print( a > b )  # Exponent Operation which results 7^3=7*7*7.
print( a < b )  # This is multiplication operation.
print( a >= b )
print( a <= b )

print( "**********************" )
#################################################################################################################
# 3. Assignment Operators
a = 7;
b = 3;

c = a + b  # Assigning to c.
c += a     # c=c+a; This is called "Short hand Assignment Operator
           # Short hand assignment operation is applicable to all other assignment operators.

print( "Shorthand operator usage:", c )

print( "**********************" )
#################################################################################################################
# 4. Logical Operators
a = 10;
b = 13;

if (a==7 and a>1):
    if (b>10 or b==3):
        print("Nested if usage & Checking Logical Operator usage")
    else:
        print("Nested If else part usage, a&b doesnt match the condition")
else:
    print("Else part of main if block condition not met")

print (a==10)
print (not a==10)  # Usage of not operator

print( "**********************" )
#################################################################################################################
# 6.Membership Operators- in & not in

a=[1,20,3,54]

print("Checking 1 in list:",1 in a)
print("Checking 200 in list:",200 in a )
print("Checking 3 not in list:",3 not in a )

print( "**********************" )
#################################################################################################################
# Identity Operator - is, is not
# If two or more objects referring to same value in memory.

a=10
b=10  # a,b are int objects referring to same value in memory location.
c=30

print("Checking for Identity Operator usage:",a is b)
print("Checking for Identity Operator usage:",a is not b)
print("Checking for Identity Operator usage:",a is c)

#################################################################################################################
# Precedence of operators pls refer below link -- PEMDAS (Parenthesis, exponent, multiplication, division, addition, subtract)
# https://www.programiz.com/python-programming/precedence-associativity




