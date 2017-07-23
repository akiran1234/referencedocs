# Large set of files can be segregated into directories.
# Directories help in  managing  the code in more organised way.
# "os module" and it's methods are very useful in managing the directories and files.

import os
print(os.getcwd())      # This will print the current working dir.
print(os.listdir())     # Print the list of files in the current working dir.
# os.rmdir("C:\Dummy")  # Removes only an empty dir, if files exist first delete the files and then dir.
# os.chdir("C:\\Dummy") # This will change the current dir to specified directory.

