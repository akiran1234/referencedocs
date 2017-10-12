# Modules are nothing but python scripts with .py extension.
# A module can define variables, functions and classes and a module can also include runnable code.
# Grouping related code into a module makes the code easier to understand and use.
# A module can be imported using import statement.
# import module_name ==> This will import all the attributes of the module into current module.

import module_math as m        # This is nothing but running module_math.py from top to bottom in the current module namespace.
                               # Please note after importing print statements from "SampleTest" module is printed in the current module.
from module_hello import hello,welcome,a
                               # The above import statement will import only specified functions to current namespace and no other attributes are imported.
                               # Please note after importing print statement of module_hello executed.
                               # Using this statement module name is not required, directly function name can be used to refer that module.
# from module_hello import *   # This * will pull all the attributes and functions in to current workspace. But this will create ambiguity problem with other
                               # (cont..) modules hence this is not best practise.

print('Printing y value from SampleTest Module',m.y)
print('Printing x value from SampleTest Module',m.x)

print(m.add(10,20))
print(m.mul(100,20))
print(m.sub(10,10))

print(hello())
w=welcome()
print(w)
print(a)