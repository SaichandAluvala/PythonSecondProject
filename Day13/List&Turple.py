
a=[1,2,3.5,"Saichand"]
b=(1,2,3.5,"Saichand")

print(type(a))
print(type(b))

print(a[1]) #2
print(b[0]) #1

print(b[1:3]) #2,3.5
print(b[:3]) #1,2,3.5
print(b[1:]) #2,3.5,"Saichand"

a[0]=True
print(a)
"""
b[0]=True #error
print(b)
"""

#insert::: is used to enter the values as per Index
a.insert(0,"Hello")
print(a)

#b.insert(0,"World") #error

#append:::  is use to enter the values at the end of the list
a.append(False)
print(a)

#print(b.append(True))

#extend ::: used to add multiple values at the end using other list
p=[1, "String", True, 3.5, 1]

a.append(p) # ['Hello', True, 2, 3.5, 'Saichand', False, [1, 'String', True, 3.5, 1]]
print(a)

a.extend(p) # ['Hello', True, 2, 3.5, 'Saichand', False, 1, 'String', True, 3.5, 1]
print(a)