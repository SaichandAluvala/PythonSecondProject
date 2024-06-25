#variables

_b=-10
print(_b)
print(type(_b))

name="Saichand"
print(name)
print(type(name))
"""
status=True
print(status)
print(type(status))

Percentage=70.5
print(Percentage)
print(type(Percentage))
"""

print("Saichand", end=" ")
print("Aluvala")

print("Saichand", "Aluvala", sep=",")

print("Saichand", "Aluvala", sep="&&")

print("Saichand", "Aluvala", sep="\n")

a=input("Enter a number")
print(a)

a,b=input("Enter your numbers"). split()
print(a,b)


print(a+b) #input is always Str ( 1020 )


a=int(input("Enter your a number"))
b=int(input("Enter your b number"))
print(a+b)

name,hobby=input("Enter your name and Hobby").split()
print(name, hobby, sep="\n")


print(5,6,7, end="   ", sep="*")



print(5<<1)