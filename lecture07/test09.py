var1 = (10, 20, "hello", True,[111,'wow'], "mana")

var2 = var1
var3 = var1.copy()

print(var1)
print(var2)
print(var3)
print()
var2[0] = 111
print(var1)
print(var2)
print(var3)
print()
