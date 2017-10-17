# Caliculate the avg of numbers in a list

l = [10, 10, 10, 10]
sum=0

for i in l:
    sum= sum + i


length=len(l)
print("Sum of list={0}  length of list={1} and avg of list={2}".format(sum,length,sum/length,'\n'))

###########################################################
# Implement the formulae : n+nn+nnn
n=int(input("Please enter the number for 'N' "))
n1=n*n
n2=n*n*n

print('Printing the output for formulae n+nn+nnn is:{0}'.format(n+n1+n2))

