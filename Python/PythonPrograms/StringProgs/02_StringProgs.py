# To remove a specific character from a given string.
s="histring"
first=s[:4]
last=s[5:]
append=first+last
print(first,last,append)

# To swap first and last chars of a string

fchar=s[0]
lchar=s[-1]
substr=s[1:-1]

final=lchar+substr+fchar
print('Swaping of first and last chars:',final)

# To find count the no of Vowels in a string

s1='an apple i am'
count=0

for i in s1:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count=count+1

print(count)

# Replace blank space with '-'

s2='an apple i am'

print("Replaced blank with '-':",s2.replace(' ','-'))

# To find count of string with out using functions

s1='an apple i am'
length=0

for i in s1:
    length=length+1

print("Length using for loop:",length)

# copy the odd index values into different string
s1='an apple i am'
final=''
count=0
for i in s1:
   count=count+1
   if (count%2 == 0):
     final = final + i

print("Printing odd index values:",final)

# Caliculate no of characters and words in a string.

s1='an apple i am'
char_count=0
word_count=1
for i in s1:
   char_count=char_count+1
   if (i == ' '):
       word_count=word_count+1

print("Printing Char count={0} and word count={1}:",char_count,word_count)

