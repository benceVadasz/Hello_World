def hello(greeting, name ="World!"):
    return '{}, {}'.format(greeting, name)

print(hello('Hello', 'Bence'))
print(hello('Hello'))