# This program will count the no of digits in a given number

a=12345
count=0
q=12345
while(a>0 and (a%10)!=0):
    count=count+1
    a=a//10

print(count)