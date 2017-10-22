#################################################################################################################
# https://www.programiz.com/python-programming/file-operation
# Python provides basic functions and methods necessary to manipulate files by default.
# File manipulation can be done only using a file object.
# import os; cwd = os.getcwd() -- to check current working directory.
# open() is a builtin function to - open a file in  read/write/append/binary  mode.
# files which doesn't have ascii characters and contain pictures/pdf/videos are read in binary mode.
# open() function returns a file object which belongs to class- '_io.TextIOWrapper' (Doubt how open() builtin function related to this class)
# obj.read(),obj.write(),obj.close() are the methods used to perform operations on files which belongs to class- '_io.TextIOWrapper'
# Syntax of open function- file_object = open(file_name , access_mode, buffering])
# file_object has various methods and attributes which can be performed on fileobject.
#################################################################################################################
# f = open("test.txt")                # open file in current directory
# f = open("C:/Python33/README.txt")  # Specifying absolute path to open the file.

f1=open('sample.txt','r')      # open is the only function to read/write/append the file and we have to specify the mode of the file.If no file throws exception.
print(f1.read())               # Printing the content of the file using read method.
# f1.write("I am overwriting") # The file i have opened is in read mode so this write operation is not possible.
f1.close()                     # Every open file has to be closed and it is a must.

# open, read, close
print( " 1 **********************" )
#################################################################################################################
# f2=open('sample_1.txt','r') --> File doesn't exist so cant execute hence open in write mode to create new file.
# f2=open('sample_2.txt','r+') --> mode is combination i.e using + is a combination (reading and writing)

f2=open('sample_1.txt','w')    # This will create the file, if file already exists it will overwrite the data (Truncate).
f2.write("Hello this is a sample text using write method\n")
f2.close()                     # Closing the file.
# print(f2.read())             # Since the file is opened in write mode this cannot read the file.

f2=open('sample_1.txt','r')    # Opening the created file
print(f2.read())               # Accessing the file data using read method.
f2.close()                     # Close the open file and it is a must.


# open, write, close, read, close
print( " 2 **********************" )
#################################################################################################################
f2=open('sample_1.txt','a')          # Opening the file in append mode
f2.write("This line is getting appended to exist\n")
# print(f2.read())                   # File opened in append mode hence cant read the file.
f2.close()

# open, append, close
#################################################################################################################
f2=open('sample_1.txt','r')          # Checking the appended data using read mode
print(f2.read())
f2.close()

print( " 3 **********************" )
#################################################################################################################
# + is a combination mode for both read and write.
f3=open('file1.txt','w+')            # file1.txt doesn't exit, creating now.
f3.write("This is a new file!!")     #
f3.close()
# print(f3.read())

f3=open('file1.txt','r')             # file1.txt doesn't exit, creating now.
print(f3.read())                     #
f3.close()

print( " 4 **********************" )
#################################################################################################################
# with statement with open() function
# By using with statement, we don't need to explicitly call the close() method. It is done internally.

with open('withfile.txt','w',buffering=1,encoding='utf-8') as w1:
    w1.write("I am using with statement\n")
    w1.write("This is the second line of with file\n")

# In the above code close() method is not used and with will do it internally.

print(w1.closed) # prints true if the file is closed. Closed is an attribute of file object.

# read the withfile.txt to check the data using with statement.
with open('withfile.txt','r') as f1:
    print(f1.read())

print( " 5 **********************" )
#################################################################################################################
# frequently used methods and attributes of a file object

print(f1.closed)    # Attribute used to check if a file is opened/closed with it's object.
print(f1.mode)      # Attribute used to check in which mode (r/w/a) the  file is opened using it's object.
print(f1.name)      # Attribute used to check the file name associated with  the object.

print( " 6 **********************" )
#################################################################################################################
# For more file methods refer- https://www.tutorialspoint.com/python/file_methods.htm

with open('withfile.txt','r') as f1:
    print(f1.read(10))    # This will read the specified characters from the beginning of the file to end of the file.
    # print(f1.read(5))    # Note, to print this the pointer position is at 10 char from previous read hence it will print next 5 chars from 11 character of the file.

print( " 7 **********************" )
with open('withfile.txt','r') as f1:
    print(f1.readline())   # This method reads a file till the newline, including the newline character.
    print(f1.readline())   # The position of the cursor is at second line and print the line until it reach '\n' character.





