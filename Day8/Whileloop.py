#swapping 2 nors in python

a,b=input("Enter two numbers").split()
print("Before swapping ",a,b)

a,b=b,a
print("After swapping ",a,b)

for x in range(5):
    print(x)

for y in range(0,4):
    print(y)

print("Z values by using step 1")
for z in range(2,5,1):
    print(z) #2 3 4

print("Z values by using step 2")
for z in range(2,5,2):
 print(z, end=",") #2,4

for num in range(5, 15, 5):
 print(num, end=",")

for z in range(1,10,3):
 print(z, end=",")


