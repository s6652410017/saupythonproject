def InputValue():
    id = str(input(" Enter ID: "))
    name = str(input(" Enter Name: "))
    salary = int(input(" Enter Salary: "))
    return id, name , salary
def Calsalary(salary):
    compleaatsalary  =  salary  -(salary * 7 / 100) -500
    return compleaatsalary
def Shwocompleatsalary(id,name,compleatsalary):
    print(f"{id}:{name}:Salary={compleatsalary}$ ")

id,name,salary = InputValue()
compleatsalary = Calsalary(salary)
comsal=Shwocompleatsalary(id,name,compleatsalary)