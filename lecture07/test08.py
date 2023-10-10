var2    = (10, 20, "hello", True,[111,'wow'], "mana")

# var2[2] = "hi" error
# การเปลี่ยนแปลงคำ เพิ่ม ลบ ข้อมูลไป Tuple
# List(), Tuple()
vartemp = list(var2)
vartemp[2] = "hi"
var2 = tuple(vartemp)
print(var2)