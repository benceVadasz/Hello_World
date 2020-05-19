import sys

def hello(name):
    if len(name) == 1:
        return "Hello World!"
    elif len(name) == 2:
        return "Hello, " + str(name[1]) + "!"
 
name = sys.argv
print(hello(name))