# Indentation Example

a = 10
b = 20

if a > b:
    print("a is greater than b")
    print("all the print statements are aligned in same order")
    print("This three print stms are aligned in same order which represents one block")
else:
    print("This is else block")
    print("B is greater than a", b)
    print("all this three print statements form else block")

# Decision Making using if else statement to execute block of code
a=-1
b=20
c=30

#################################################################################################################
# if else example
if (a>0):  # colon required and indent should be maintained
    print("A is positive:",a)
else:      # colon required and indent should be maintained
    print("A is negative",a)

print( " 1 **********************" )
#################################################################################################################
# Indentation Example

a = 10
b = 20

if a > b:
    print("a is greater than b")
    print("all the print statements are aligned in same order")
    print("This three print stms are aligned in same order which represents one block")
else:
    print("This is else block")
    print("B is greater than a", b)
    print("all this three print statements form else block")

print( " 2 **********************" )
#################################################################################################################
# Nested if
a=10
b=2
c=30
d=40

if (a<0):
    print("In Main if block",a)
    if(b>=20):                           # if satisfied inside if block will be executed and else block will be skipped
        print("Inner if of Main if:",b)
    else:
        print("Inner if else block:",b)
    print( "In Main if block", a )       # This print stmt belongs to main if block and after execution of inner if else this stmt will be executed.
else:
    print("In main else block:",a)
    if(c>30):
        print("Inner if of main else:",c)
    else:
        print("Inner if of else block:",c)
    print( "In main else block:", a )    # This print stmt belongs to main else block and after execution of inner if else this stmt will be executed.

print( " 3 **********************" )
#################################################################################################################
# if elif else
# if condition pass exit the block. if conditions fails then check elif condition and so on..
# Condition satisfied in any block it will exit the block (if elif else)

a=10
b=2
c=30
d=40

if (a<0):                                      # if cond true exit the complete block, false go to elif
    print("Main if block")
    print("Exiting the if elif else check")
elif (a>0 and a<5):                            # if cond true exit the complete block, false go to next elif and so on ..
    print("First elif block:",a)
    print("Exiting the if elif else check ")
elif (b==2):                                   # if cond true exit the complete block, false go to next elif and so on ..
    print("Second elif block",b)
    print("Exiting the if elif else check")
else:                                          # if none of the above blocks is true, else will be executed
    print("Main else block")

