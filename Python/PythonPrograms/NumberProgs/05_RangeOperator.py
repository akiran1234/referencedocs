# for i in range(1,5):  --> Range operator iterates n-1 times hence 5-1=4 times.
#    print(i)

# Provide the range of numbers and print which is divisible by 2 with in the range.

l_range=int(input("Enter the lowest range="))
h_range=int(input("Enter the Highest range="))
n=int(input("Enter the number that has to be divisible="))

for i in  range(l_range,h_range):
    if(i%n==0):
        print("Number's divided by {0} with in the range={1}".format(n,i))
    else:
        print("Numbers not divided by {0} with in the range={1}".format(n,i))

