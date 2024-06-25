
#Sets
s = {1,2,3.5,"Saichand"}
print(s)
print(type(s))

#cannot print single value in Sets
#print(s[0])

#cannot assingment/change the values in Sets
#s[0]=3
#print(s)
"""
s = {1,2,3.5,"Saichand"}
for i in range(100):
    print(s)
"""

#add the value to Sets
s.add(12)
print(s)

#True can be add to sets but It is not adding --any update
s.add(True)
print(s)

#remove the value from sets
s.remove(2)
print(s)
