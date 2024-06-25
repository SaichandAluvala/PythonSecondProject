
#Break and Continue

#continue-- only skip the if condition true
print("Continue statement will be started from here")
n=0
while n<10:
    if n==2:
        n += 1
        continue
    print(n)
    n+=1

#break -- break the loop irrespective of while condition
print("Break statement will be started from here")
n=0
while n<10:
    if n==2:
        n += 1
        break
    print(n)
    n+=1

