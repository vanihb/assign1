setone={2,4,6,8}
print(setone)
print("add method")
setone.add("10")
print(setone)
print("copy method")
settwo=setone
setone.add(12)
print(settwo)
print(setone)
print("set difference method")
setthree={1,3,4,6,10}
print(setone.difference(setthree))
#or setone-setthree
print(setthree.difference(setone))
print("intersection ")
print(setone.intersection(setthree))
print("union method")
print(setone.union(setthree))
print("remove method")
print(setone.remove(8))
