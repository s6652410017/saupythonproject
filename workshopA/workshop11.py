def inputNamePhonenumAndTime():
    name = str(input("Enter name: "))
    phone = str(input("Enter phonenumber: "))
    time = int(input("Enter Time to use: "))
    return name,phone,time

def Calamountmoney(time):
    if time >= 31 :
        cost = time * 1.50
        return cost
    elif time >= 16 and time <= 30 :
        cost = time * 3
        return cost
    elif time >= 1 and time <=15 :
        cost = time * 5
        return cost
    else:
        return "No Resault"


def showresault(name,phone,time,cost):
    print(f"Name: {name} phonenum:{phone} ")
    print(f"Time to use:{time} minuet price:{cost}Baht ")

name,phone,time = inputNamePhonenumAndTime()
cost=Calamountmoney(time)
showresault(name,phone,time,cost)