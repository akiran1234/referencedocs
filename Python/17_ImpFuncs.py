# Important function in python

# range function will generate numbers as per the given range.
# range(start,end,step) # Will generate range of numbers from the given start and end points and iterates (end-1) times.
# Start is starting number and end is ending number and step is increment number. If step is + from beginning and step is -ve from ending.
# range is called as xrange in Python 2x and in Python 3x it is range hence xrange wont work in python 3.

for i in range(1,10,1):   # Increment by 1
    print(i)
print("***********")

for i in range(0,-10,-1): # Decrement by 1
    print(i)

for i in range(1,10,2):   # Increment by 2
    print(i)
print("***********")


# enumerate function -> used to iterate through the sequence object and retrieve the index position and its corresponding value at the same time.

s='hellokira'
for i,j in enumerate(s):
    print("enumerating with position={0} and its value={1}".format(i,j))

# eval()  evaluates the expression and gives the result.
x=100
print(eval('x+1'))


# Zip function will combine two iterable objects and results in set format.

list1 = ['A','B','C','d']
list2 = [10,20,30]
res=zip(list1,list2)
print("Zipped result in set format={0}".format(set(res)))     # O/P: {('B', 20), ('A', 10), ('C', 30)}

# random is a module to generate random numbers.
import random
print(random.randrange(1,1000))  # randrange is function which generates one random number with in the range.

# Iterators

# generators

# decorators

# closures