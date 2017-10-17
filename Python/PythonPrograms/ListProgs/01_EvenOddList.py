# This prog is to print 1 st max,2nd Max, min values and even and odd values in a different list

l1=[10,-5,2,3,10,20,100,9,22]

l1.sort()
print('1sr Max value',l1[-1])
print('2nd Max value',l1[-2])
print('Minimum value',l1[0])

lodd=[]
leven=[]

for i in l1:
    if(i%2==0):
        leven.append(i)
    elif (i%3==0):
        lodd.append(i)
    else:
        pass

print('Even list',leven)
print('odd list',lodd)

# Merge two lists

l2=[1,2,3,4]
l3=[5,6,7,8]

l2=l2+l3
l2.sort()
print("L2 and L3 merged and sorted",l2)

# Sort using sort key sort arguments sort(self,key,reverse)

l4=['abcdefghij', 'abcd', 'abcdefg', 'Red']
l4.sort(key=len)  # Sorting using length of elements
print(l4)
l4.sort(reverse=1) # Sorting in reverse order
print(l4)

# insert the elements into list in such a way it should have square of its numbers

square=[]
for i in range(1,5):
    square.append(i**2)

print(square)

# Swaping of first and last element in a list

l1=[1,2,3,4]

print('Before Swap',l1)

l1[0]=l1[0]+l1[-1]  # 5
l1[-1]=l1[0]-l1[-1] # 1
l1[0]=l1[0]-l1[-1]

print('After Swap',l1)

# Generating random numbers from random module

import random
a=[]

for j in range(10):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)