listone = ["hockey","cricket","tennis","athletics","football"]
print(listone)
print("access list elements")
print(listone[0])

print("slicing")
print(listone[:])
print(listone[3:])
print("length of list")
print(len(listone))
print("types of elements in list")
print(type(listone))
print("insert elements")
listone.insert(2,"kabadi")
print(listone)
print("append method")
listone.append("cricket")
print(listone)
print("remove method")
listone.remove("tennis")
print(listone)
print("sort the list")
listone.sort()
print(listone)
print("reverse order of list")
listone.reverse()
print(listone)
print("copying list")
listtwo=listone.copy()
print(listtwo)
print("index method")
listone.index("cricket")
print("count of item in the list")
print(listone.count("cricket"))
print("extend method")
listthree=[1,2,2,3]
listone.extend(listthree)
print(listone)
print("pop method")
listone.pop(3)
print("clear the list")
listone.clear()
