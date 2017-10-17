#################################################################################################################
# d1={'name':'python','age':23,'salary':10000.45}
# Dictionary Datatype items are represented with curly braces in key-value fashion. Key and Value separated with colon (:) and enclosed in single quotes.
# Here keys (name,age,salary)  are unique and corresponding values can be unique/duplicate.
# If a key is duplicated the last duplicate key is considered. Ex: d1={'name':'python','age':23,'salary':10000.45,'name':'Linux'}
# Dictionary data type is mutable (changeable) hence it's items can be modified- updated,deleted,insert and so on..
# Accessing the items of dictionary will be with keys and slice operator but not with indexing like strings,list and tuple.
# We cannot access range of items from dictionary as we did with string,list and tuple.
# We can access only one element from dictonary at a time.
# Concatenation (+) and Repetition (*) operator is not supported.
#################################################################################################################
# Defining Dictionary

d1={'name':'Linux','age':23,'price':2343.23}
print("Checking the datatype of d1:",type(d1))
print("Printing d1 values:",d1)

d2={'name':'Linux','age':23,'price':2343.23,'name':'Unix'}
print("Duplicate key name referring to last key:",d2)           # Here name is duplicated and the last one is referred.

# Accessing the items of dictionary


d2={'name':'Unix','age':33,'price':99.00}
print("Accessing dictionary with key:",d2['name'],d2['age'])    # Accessing  dictionary item with key and it should be single.

d3={1:'hyd',2:'ibm',3.5:123}                                    # Defining keys in numeric and float
print("Keys defined in Numeric:",d3)
print(d3[1],d3[2],d3[3.5])                                      # Accessing with keys which is in numeric and float

print("**********************")
#################################################################################################################
# Modifying dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First',12.4:'last'}

print(dict)
del dict['Name']              # remove entry with key 'Name'
print(dict)

dict['location']='bangalore'  # Inserting new item which will be appended at the end.
print(dict)

del dict ;                    # delete entire dictionary but still it exists
print(type(dict))

print("**********************")
#################################################################################################################
#  Functions of builtin module can be applied
dict11 = {'Name': 'Zara', 'Age': 7, 'Class': 'First',12.4:'last'}

x=len(dict11)       # Finds the length of dictionary
print(x)

print(str(dict11))  # which will represent in string format
print(dict11)

print("**********************")
#################################################################################################################
# Methods of Dictionary class

# Refer-->  https://www.tutorialspoint.com/python/python_dictionary.htm
##################################################################################################################
# Set Data which is represented in curl braces {}
# Items of the set are immutable i.e values cannot be changed
# We cannot access set items individually by slice operator.
# Set operations can be performed --> union, intersect, difference and so on..

s1={1,3,'kiran',344.55}
print(type(s1))

# There are built in functions and methods and can be refereed from the below link.
# https://www.programiz.com/python-programming/set
