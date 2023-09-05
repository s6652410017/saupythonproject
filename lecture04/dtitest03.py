#function แบบที่ 2 - have parameters/No return
#parameters คือ เป็นตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใฃ้เฉพาะในฟังก์ฃั่นนั้นๆ เท่านั้น

def funcA( x,y) :
    print(f'x 1s {x}')
    print(f'x 1s {y}')
    print(f'Sum  {y} + {y} = {x+y}')
    
funcA(10, 20) #call function ข้อมูลที่ส่งให้ parameter เรียกว่า argument
funcA(1, 4)
print('DTI......')
funcA(5, 5)