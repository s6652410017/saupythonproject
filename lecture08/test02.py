#list มีลำดับ
my_list = [10,20,30, True, (10,"hello"),[10,20],("SAU","DTI")]

#Tuple
my_tuple = (10,20,30, True,(10,"hello"),[10,20],{"SAU","DTI"})

#set
my_set = {10,20,10, True,("hi")}
                
                
                #Key คือ index คือคำที่อ้างอิงไปยัง Value
                #value คือ ค่าข้อมูลที่สามารถใฃ้งานได้   

                            

#Dictionay ---> Key:value / Key -> string-Number / value-> Everthing
my_Dic = {'name':'สมฃาย','age': 20, 555:999, 'flag': True}
print(my_Dic("name"))
print(my_Dic["age"] + my_dict[555])
my_dict["name"] = "สมหญิง"
my_dict["major"] = "DTI"
print(my_Dic)
my_Dic.pop("name")
my_Dic.pop(555)
print(my_DIc)
my_Dic.popitem
print(my_Dic)




for data in my_Dic:
    print(data, end="")

print()

for data in my_Dic.key:
    print(data, end="")

print()

for data in my_Dic,value():
    print(data, end="")

my_Dic1 = {"A":70, "B":20, "C":30}

my_Dic2 = my_Dic1

my_Dic3 = my_Dic1.copy()


print()
print(my_Dic1)
print(my_Dic2)
my_Dic2["A"] = 999
my_Dic3["A"] = 777
print(',,,,,,,,,,,,,,,,,,,,,')
print(my_Dic1)
print(my_Dic2)
print(my_Dic3)