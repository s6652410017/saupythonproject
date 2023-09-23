def InputIdNameAndamoutmoney():
    id = str(input("Enter ID: "))
    name = str(input("Enter name: "))
    money =  int(input("Enter money: "))
    return id,name,money

def CalCommission(money):
    if money >= 3001:
        commission = money * 0.05
        return commission
    elif money >= 2001 and money <= 3000:
        commission = money * 0.03
        return commission
    elif money >= 1001 and money <= 2000:
        commission = money * 0.01
        return commission
    else:
        return 0.0 

def showresault(id,name,money,commision):
    print("-----------------------------")
    print("        COMMISSION           ")
    print("-----------------------------")
    print(f"ID: {id} ")
    print(f"Name: {name} ")
    print(f"Money: {money} ")
    print(f"Commission: {commission} ")

id,name,money =InputIdNameAndamoutmoney()
commission = CalCommission(money)
showresault(id,name,money,commission)