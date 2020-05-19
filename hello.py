import sys

def hello(greeting, name ="World!"):
    return '{}, {}'.format(greeting, name)
    if name == None:
        return "World!"

print(hello('Hello', 'Bence'))
print(hello('Hello'))

print(sys.argv[0])