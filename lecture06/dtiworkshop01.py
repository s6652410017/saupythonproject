#dtiworkshop01.py
#โปรแกรมคำนวนพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์และแสดงผลพื้นที่สามเหลี่ยมที่คำนวนได้ทางหน้าจอ

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อที่จะไปสร้างเป็น function
#1. รับค่า ฐาน สูง
#2. คำนวนพื้นที่ และแสดงผลออกมา

def inputBasehigh() :
    base = float( input('ป้อนฐาน : '))
    high = float( input('ป้อนสูง :'))
    return base, high

def calAndShowTriangleArea(base, high) :
    area = base * high / 2 
    print(f'สามเหลี่ยมพื้นฐาน {base} สูง {high:.2f} มีพื้นที่ {area:.2f}')

print('.......................')
print('Calculate Triangle Area')
print('.......................')
base, high = inputBasehigh()
print('.......................')
calAndShowTriangleArea(base, high)
print('.......................')