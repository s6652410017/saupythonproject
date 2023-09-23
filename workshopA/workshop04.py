def SetFunction(x):
    y = 2 * x**2 + 2 * x + 1
    return y

def inputValuex():
    x = float(input("Enter the value of x: "))
    return x

def Showy(y):
    print(f"Equation y is:{y} ")

x = inputValuex()
y = SetFunction(x)
Showy(y)