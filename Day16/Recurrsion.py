
#Recurrsions

def factoria(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factoria(n-1)

print(factoria(3))

#Assignments

#power of the number 2^3=2*2*2=8
 #2^3=2*(2^2)*(2^1)  where x=2, n=3

#Assigments -- power ( x,n) --5^3=5*5*5
def powe(x,n):
     if n == 1:
         return x
     else :
         return x*powe(x,n-1)

print(powe(5,3))

#Assignment --- Fibannoci series from 0 to 100


dummy1=0
dummy2=1
for i in range(0,5):
 print(dummy1, dummy2, end=" ")
 dummy1=dummy1+dummy2
 dummy2=dummy2+dummy1

