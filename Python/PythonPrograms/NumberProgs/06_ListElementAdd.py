# Print the elements of the list whose sum is 5.

d=[1,2,3,5]
l=len(d)
print('Length of the list={0}'.format(l))
for i in range(0,l):
    #print(d[i])
    for j in range(0,l):
        #print(d[j])
        if(d[i]+d[j]==5):
            print('Sum of this elements {0},{1}={2}'.format(d[i],d[j],d[i]+d[j]))

# With for loop

d=[1,2,3,5]
l=len(d)
print('Length of the list={0}'.format(l))
for i in d:
    #print(d[i])
    for j in d:
        #print(d[j])
        if(i+j==5):
            print('Sum of this elements {0},{1}={2}'.format(i,j,i+j))



# Below program will print all the possible combinations of the list
print('printing possible combinations') # Like (123,124,125) and not like (111,222,333)

for i in range(0,l):
    for j in range(0,l):
        for k in range(0,l):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])