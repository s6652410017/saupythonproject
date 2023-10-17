# List
my_list = [10,20,30, True, False, "sale"]
print(my_list)


#tuple
my_tuple = (10,20,30, True, False, ("sale"))
print(my_tuple)


#set
my_set = {10,20,30, True, False,("hi")}
print(my_set)
print(len(my_set))

for data in my_set : 
    print(data, end='/')

print(',,,,,,,,,,,,,,,,,,,,,,,')

listformat = list(my_set)
print(listformat)
listformat[0] = "DTI"
my_set = set(listformat)
print(my_set)
my_set.clear()
print(len(my_set))

my_set1 = (10, 20 ,30, "hi")
my_set1 = {10, "hello" , "hi", True}

my_set1.add(999)
print(my_set1)
my_set.remove("hi")
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

#len, min, max
print(min(my_set2))