# Important string methods

s='hi hello string'

# s.count('substr',strtindex,endindex)  substr=string that has to be searched;
print('No of sub string occurrences=',s.count('h'))  # By default start index will be 0 and end index will be the length of the string.


# str.index(str, beg = 0 end = len(string))          # Will provide the index position of substring.
print("Print the index number of 'll'=",s.index('ll'))

# str.find('substr')                                 # find will search for a sub string in the main string and returns index if found else returns -1.
print('Find for a substring= ',s.find('x'))


# str.replace(old, new)                              # This will replace old string with new string.
print('Replace method=',s.replace('hello','123'))

# substr.join(obj)                                   # Will join the provided substr with string object
print('Joins the substring with string=','|'.join(s))# h|i|h|e|l|l|o

# s.split('delimiter')                               # This method will split the delimited string for the provided delimiter.
s1="This,is,delimited,string"
s2=s1.split('|')                                     # split method return type is list.
print('Spliting delimited string:',s2,type(s2))


# str.maketrans(intab, outtab)                       # This fn will translate the characters. intab=actual characters outtab=mapping characters
# print('Translate',s.maketrans('hs','12'))          # Not working check

# s.upper(), s.lower()
print("Print upper and lower:",s.upper(),s.lower())

# str.isalnum(); str.isalpha(); str.isdigit(); str.islower(); str.isnumeric(); str.isspace(); # Return true/false of the string.
print('isalpha check=',s.isalnum())

# s.__len__()                                        # Find the length of the string object and len() is builtin function.
print(s.__len__())