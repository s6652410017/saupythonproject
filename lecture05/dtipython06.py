#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง เป็นการบ่งบอกการทำงานนั้นๆ ว่าเสร็จแล้ว
def exampie1():
    print(111) 
    print(222) 
    return
    print(3333)
    print(4444)
    return

# default parameter
def dtitest(x = 99 ,y = 0, z = 20, a = 10) :
    print(f'{x}+{y}+{z}+{a}={x+y+z+a}')
    
    
    dtitest(5, 100)
    
    dtitest(9, 8, 10)