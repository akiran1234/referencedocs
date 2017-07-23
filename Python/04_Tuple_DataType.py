#################################################################################################################
# Tuple Datatype which is defined using parenthesis () and values are separated by comma (,).
# Tuple is defined using parenthesis (), List is defined using square brackets [].
# Tuple is a immutable (not changeable) data sequence object.
# Tuple of elements can be accessed using indexing the same way a string and list is accessed.
# Index starts with 0 and end with length of tuple-1. Accessing of the tuple in reverse direction using -1, -2 and so on..
# Single element of a tuple also should be separated with comma (,). Ex: a=(99,)
#################################################################################################################
"""putting in the quotes has no effect on execution"""  # This is called doc string.

t1=(10,20,'first',11.45)   # Tuple representation with ().
print("Printing tuple values:",t1)

t2=(22,)
print("Single element representation in tuple:",t2)
print("Checking the data type of t2:",type(t2))

t3=(12)                    # Single element with out comma so this is not a tuple.
print("Checking the data type of t2:",type(t3))

print("**********************")
#################################################################################################################
# Accessing the tuple values using slice operator and indexing.

t4=(10,99.45,1,3,'tuplelast')

print(t4[0])   # Extracting first value
print(t4[-1])  # Extracting Last value.
print(t4[3])   # Extracting fourth value
print(t4[:4])  # From 0 position to 3rd position excluding 4th position in the list
print(t4[1:])  # From second value to till end of the list.

print("**********************")
#################################################################################################################
# Tuple is immutable hence update and delete of tuple elements is in valid.

t5=(10,30,3.45,11,56)
# t5[0]=99  # Tuple update is in valid
# del t5[-1]  # Tuple item deletion is invalid.

#################################################################################################################
# Tuple Operators (Similar to String & List operators)
# +              --> Concatenation operator, which will concat two or more list objects and display as single list.
# *              --> Repetition operator,    which will create new list by repeating multiple copies of the same string.
# []             --> Slice operator,         Will give the character from the given index.
# [:]            --> Range Slice operator,   will give the character's from the given range.
# in             --> Membership operator,    Returns true if character exists in the given string.
# not in         --> Membership operator,    Returns true if character doesn't exists in the given string.
# for x in list:  -> Iteration Operator,     Which will iterate and prints the results
#################################################################################################################

t8=(1,2,'a',23.55,'t3-last')
t9=(9,10,11,'python','t4-last')

print("Concatenating t8 and t9:",t8+t9)
print("Repetition operator on t8:",t8*3)
print("Slice operator on t8:",t8[-1])
print("Range Slice operator on t8:",t8[2:])
print("Membership operator in t8:",23.55 in t8)
print("Membership operator in t8:",'a' not in t8)

for x in t8:
     print("-----------------------------------------------")
     print("Printing tuple elements through for operator:",x )
     print("===============================================")

print("**********************")
#################################################################################################################
# Tuple function similar to list

# t10, t11 = [123, 'xyz'], [456, 'abc'] --> This list cannot be applied for functions as it is having int  and str data types.
t10=(1,2,3,4,'last')
t11=('abc','xyz')
# print(cmp(list1, list2))  # Not working
print(len(t10))
print(min(t11))
print(max(t11))

print("**********************")