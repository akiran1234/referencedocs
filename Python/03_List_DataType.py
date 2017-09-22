#################################################################################################################
# List Datatype which is represented using square brackets [] and values are separated by comma (,).
# List is the most versatile data type used in python
# List is a mutable (changeable) data sequence object
# List of elements can be accessed using indexing the same way a string is accessed.
# Index starts with 0 and end with length of list-1. Accessing of the list in reverse direction using -1, -2 and so on..
#################################################################################################################

list1=[12,"Linux",34.556,'a',10,'Last']
print("Printing the list values:",list1)

# Accessing the list values using indexing.
print("**********************")

print(list1[0])   # Extracting first value
print(list1[-1])  # Extracting Last value.
print(list1[3])   # Extracting fourth value
print(list1[:4])  # From 0 position to 3rd position excluding 4th position in the list
print(list1[1:])  # From second value to till end of the list.

print("**********************")
#################################################################################################################

# Deleting list using del statement.
# del list1; del list1,list2 # Multiple delete
# print(list1)

# List is mutable hence updating and deleting the list elements is valid.


list2=['a',1,12,34,45,'last']
print("Printing list2 values={0} and length is= {1}".format(list2,len(list2)))
del list2[0]
print("After deleting the first element of list2:{0} and length={1}".format(list2,len(list2)))

list2[1]=999 # Updating the list elements
print("After updating  2nd element with 999 in list2={0}".format(list2))

print("**********************")

#################################################################################################################
# List Operators (Similar to String operators)
# +              --> Concatenation operator, which will concat two or more list objects and display as single list.
# *              --> Repetition operator,    which will create new list by repeating multiple copies of the same string.
# []             --> Slice operator,         Will give the character from the given index.
# [:]            --> Range Slice operator,   will give the character's from the given range.
# in             --> Membership operator,    Returns true if character exists in the given string.
# not in         --> Membership operator,    Returns true if character doesn't exists in the given string.
# for x in list:  -> Iteration Operator,     Which will iterate and prints the results
#################################################################################################################

list3=[1,2,'a',23.55,'L3-last']
list4=[9,10,11,'python','L4-last']

print("Concatenating list3 and list4:",list3+list4)
print("Repetition operator on list3:",list3*3)
print("Slice operator on list3:",list3[-1])
print("Range Slice operator on list3:",list3[2:])
print("Membership operator in list3:",23.55 in list3)
print("Membership operator in list3:",'a' not in list3)

for x in list3:
     print("-----------------------------------------------")
     print("Printing list elements through for operator:",x )
     print("===============================================")

print("**********************")
#################################################################################################################
# In built functions that can be applied on list objects.
# To apply below functions all the list elements should be of same data type
# cmp(list1,list2)
# len(list)         # Displays the length of the list object, it supports any data type elements.
# min(); max(list)  # Displays the min and max value from the list of elements.
# list(seq)         # Type casting function which converts seq data type to list data type.
#################################################################################################################
# list1, list2 = [123, 'xyz'], [456, 'abc'] --> This list cannot be applied for functions as it is having int  and str data types.
list3=[1,2,3,4,'last']
list4=['abc','xyz']
# print(cmp(list1, list2))  # Not working
print(len(list4))
print(min(list4))
print(max(list4))

print("**********************")
#################################################################################################################
# List class Methods

list1=[10,20,30,40,50,'last',30]

list1.append(99)                  # Append method will append the value to the actual list at the end.
print("Appended",list1)
print("Count",list1.count(10))    # count method will no of occurrences of the provided value
print("Index",list1.index(30))    # Index will return the position of the first occurrence of value 30
list1.insert(-1,'Insert')         # This will insert the element at given position.
print("Inserted",list1)
list1.remove('last')              # This will remove the element 'last' from the list
list1.remove('Insert')            # This will remove the element 'Insert' from the list
print(list1)
list1.sort()                      # Sort method will sort the list of elements pre requite for sort is all elements should be of same data type.
print(list1)                      # Printing the sorted list.


# There are many methods refer --> https://www.tutorialspoint.com/python/python_lists.htm
#################################################################################################################


