#################################################################################################################
# Loops are used to execute a block of code repeatedly.
# we have while loop and for loop for repetitive execution.
# The block is iterated based on condition, until it is true and exits when the condition fails.
#################################################################################################################
# While loop execute this in terminal

count=0
while (count<=5):                                   # if we take a condition which never becomes false it will become infinite loop.
    print("Executing while statement and iteration=",count)
    count+=1
else:
    print("Python supports else block for loops.")  # else  block will be executed after completing while loop iterations
    print("Else  block will be executed after completing while loop iterations")

print( " 1 **********************" )
#################################################################################################################
# For loop - execute this in terminal
# To traverse and print data structures like- list, tuple & set for loop is used.
# for loop supports only list, tuple and set.
# Python doesn't support traditional for loops with loop variable. Ex: C,C++ and Java.

list1=[1,2,4,'abc',34.45]

for x in list1:
    print("Iteration in for loop,printing list values=",x)
    print("printing in for loop")

print( " 2 **********************" )
#################################################################################################################
# for loop with tuple

tuple1=[1,2,4,'abc',34.45]

for y in tuple1:
    print("Iteration in for loop,printing list values=",y)

print( " 3 **********************" )
#################################################################################################################
# for loop with Set
# Since Set is not based on indexing for loop will print items randomly in any order.

s1={10,20,30,'kiran','kumar',12.34}

for abc in s1:
    print('Set iteration using for loop:',abc)
else:
    print("for loop supports else block which will be executed at end after iterating for loop elements")


