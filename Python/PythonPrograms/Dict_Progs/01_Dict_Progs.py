# To print by iterate the keys and values of dictionary.

d2={'name':'Unix','age':33,'price':99.00}

print('Actual Dict=',d2,'\n')
print('Print only Keys=',d2.keys(),'\n')
print('Print only Values=',d2.values(),'\n')
print('Print Items=',d2.items(),'\n')

for i in d2.keys():             # Iterating only keys
    print('Keys printing in for loop:',i)

for i in d2.values():           # Iterating only values
    print('Values printing in for loop:',i)

for k,v in d2.items():          # Iterating both key and values using items method.
    print('Key={0},value={1} iteration in for loop:'.format(k,v))

d2.update({'Loc':'Blr'})        # Append/Insert New key,value pair to existing dictionary.

print('After appending using update method:',d2)

# To initialize and print the all the datatype.

s1=''
l=[]
t=()
d={}
s=set()                          # Initialize an empty set

print(type(s1))
print(type(l))
print(type(t))
print(type(d))
print(type(s))