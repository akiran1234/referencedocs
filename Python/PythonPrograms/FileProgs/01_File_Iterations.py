

with open("C:/Users/15936/Desktop/ODS/Sample1.txt", 'w',encoding = 'utf-8') as f:
    f.write("Hi this is writing in to file\n")
    f.write( "Second write statement" )

with open("C:/Users/15936/Desktop/ODS/Sample1.txt", 'r',encoding = 'utf-8') as f:
    print(f.read())


with open("C:/Users/15936/Desktop/ODS/Sample1.txt", 'a',encoding = 'utf-8') as f:
    f.write("Append line one\n")
    f.write( "Append line two\n" )

with open("C:/Users/15936/Desktop/ODS/Sample1.txt", 'r',encoding = 'utf-8') as f:
    print(f.read())

print("****************************************************************************")
with open("C:/Users/15936/Desktop/ODS/Sample1.txt", 'r',encoding = 'utf-8') as f:
    print(f.readline())