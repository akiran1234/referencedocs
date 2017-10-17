# To print the reverse of a number
n=1234
dig=rev=0

print("Actual Number={0}".format(n))
while(n>0):
    dig=n%10         # It will pull the last digit
    rev=rev*10+dig
    n=n//10          # It will pull the quotient after divided by 10.

print("Reverse of Number={0}".format(rev))

###########################################################################################
# To check a given number is palindrome or not
n=151
dig=rev=0
pal=n

print("Actual Number={0}".format(n))
while(n>0):
    dig=n%10         # It will pull the last digit
    rev=rev*10+dig
    n=n//10          # It will pull the quotient after divided by 10.

if(rev==pal):
    print("Number is palindrome={0}".format(pal))
else:
    print("Number is not palindrome={0}".format(rev))

###########################################################################################
# To print even or odd

n=7

if n%2==0:
 print('The number is even={0}'.format(n))
else:
 print('The number is odd={0}'.format(n))

 ###############################################################################################
 # Sum of numbers of a given digit.

 a = 1234
 sum = 0

 while (a > 0):
     dig = a % 10
     sum = sum + dig
     a = a // 10

 print( sum )

 ################################################################################################
 # Find the least divisor for a number

 n = 15
 a = []
 for i in range( 2, n ):
     if (n % i == 0):
         a.append( i )
 a.sort()
 print( "Smallest divisor is:", a[0] )

 ###################################################################################################
 # This will print the number which is not divisible by 2 and 3.

 for i in range( 1, 50 ):
     if (i % 2 != 0 and i % 3 != 0):
         print( "This is not divisible by 2 or 3:", i )