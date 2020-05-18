import sys


def hello(name):
    if len(name) == 1:
        message1 = "Hello, World!"
        return message1
    elif len(name) == 2:
        message2 = "Hello, " + str(name[1]) + "!"
        return message2
    else:
        name_list = []
        for arg in name[1:]:
            name_list.append(arg)
        message3 = "Hello, " + ", ".join(name_list) + "!"
        return message3


name = sys.argv

if __name__ == "__main__":
    print(hello(name))


# function included, return value used, works


'''
terminal argumentum list:
name_list = []
for arg in sys.argv[1:]:
    name_list.append(arg)
print(name_list)
print("Hello, " + ", ".join(name_list) + "!")
'''

"""
non terminal version:
def hello(name):
    if name == "" or name == " ":
        return "Hello, World!" 
    elif name is None:
        return "Hello, World!"
    else:
        return "Hello, " + name + "!"


if __name__ == "__main__":
    print(hello("name"))
"""





