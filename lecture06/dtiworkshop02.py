#วิเคราะห์
#มองหา feature การทำงานมีอะไรบ้าง เพื่อจะไปสร้างเป็น function
#รับค่าทะเบียนรถ น้ำหนักรถ -> inputcardetal
#ตรวจสอบน้ำหนักรถ และแสดงผล -> checkAndShowWeight

def inputCardetail() :
    carNo = input(' ป้อนน้ำหนักรถ :')
    carWeight = float(input(' ป้อนน้ำหนักรถ :'))
    return carNo, carWeight

def checkCarAndShowweight(carNo, carweight) :
    if carweight > 1000 :
        print(f'ทะเบียนรถ{carNo}: น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'ทะเบียนรถ{carNo} น้ำหนักผ่านเกณฑ์')

print('.......................')
print('Truck Checker')
print('.......................')
carNo, carweight = inputCardetail()
print('.......................')
checkCarAndShowweight(carNo, carweight)
print('........................')