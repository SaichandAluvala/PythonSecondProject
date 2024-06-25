#Strings

name="Saicahand"

#end parameter is used to print the string as we expected ( space b/w characters, or , or & )
for i in name:
    print(i,end=' ')

#split() is used to split the 2 numbers by space
x,y=input("Enter your numbers").split()
x=int(x)
y=int(y)
print(x,end='    ')
print(y)

name="Shirisha"
print('a' in name) #true

print('b' in name) #False

print('c' not in name)  #true

print("This is my name \n "+name) #\n new line-- \t--tabspace
print("\n") #\n
print(r"\n") #\n - RAW the string in output
print(name.upper()) #SHIRISHA
print(name.lower()) #shirisha