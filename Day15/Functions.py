#Functions in python

def function_name():
    print("Hello World")
print(function_name())

def function_name(a,b):
    print(a+b)
print(function_name(1,2))
def add(a,b):
    print(a+b)
print(add(2,3))
print(add(4,5))

#retun date into function name
def sub(a,b):
    return a-b
print(sub(3,2))

z=sub(5,2)
print(z)

#.doc is use to print multi line comments of the particular function
def main(name):
 """
    This is use to print main function
 """

 print("Helo! ", name)
print(main("Sam"))
#To use print the funcation related comments
print(main.__doc__)
