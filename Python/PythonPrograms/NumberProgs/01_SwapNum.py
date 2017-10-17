# Swaping of no's with out temp variable

a=3; b=9
print(a,b)

a=a+b # a=12  # Always add two no's and put it in a.
b=a-b # b=3
a=a-b # a=9

print(a,b)

# a,b=b,a --> Python supports this kind of assignment.