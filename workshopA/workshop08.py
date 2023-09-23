def InputnameprovinceAndPH():
    name = str(input("Enter name Province:"))
    PH = int(input("Enter Value PH:"))
    return name,PH

def checkPHshow(PH,name) :
    if   PH >= 7 and PH <= 8:
        print(f"{name}: PH = {PH}:Result is Normal")
    elif PH > 8:
        print(f"{name}: PH = {PH}:Result is Acid")
    elif PH < 7 :
        print(f"{name}: PH = {PH}:Result is Alkali")
    else:
        print(f"{name}: PH = {PH}: Result is Unknown")    
    
print("-----------------------------")
print("         PH TEST             ")
print("-----------------------------")
name,PH = InputnameprovinceAndPH()
checkPHshow(PH,name)