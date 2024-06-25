#Dictionaries

Dict={"name":"Saichand", "age":20, "Marks":70.5, "Marks2":70}
print(Dict)
print(type(Dict))

print(Dict.get("name"))
y=Dict.keys()
print(y)

for i in y:
    print(Dict.get(i))

z=Dict.values()
#print(z.get("name"))
print(Dict)

print("age" in Dict)

#add the key and value into Dictionaries
Dict.update({"class":"10th"})
print(Dict)
print("class" in Dict)
print(Dict.values())

#add the key and it's values into Dictionaries
Dict["hobbiles"]=["Playing/watching cricket and Movies", "Learn new Technologies"]
print(Dict.values())
print(Dict)

print(type(Dict.get("hobbies")))


#remove the hobbiles from Dictonaries
Dict.pop("hobbiles")
print(Dict)

Dict.pop("class")
print(Dict)