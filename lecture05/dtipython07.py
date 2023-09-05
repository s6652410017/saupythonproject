#โปรแกรมคำนวณหาพื้นที่รอบวงกลม และ ปริมาตรทรงกลม 
#จากรัศมีที่ป้อนโดยผู้ใฃ้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นร้อบ และปรัมิาตรทางหน้าจอ

#ขอ 5 ฟังก์ฃั่น
import math

#inputRadius
def inputRadius():
    r = input('ป้อนรัศมี :')
    #หรือ r = float(input('ป้อน:'))
    #return r
    return input('ป้อนR:')
    #return r
    
    #return input('ป้อนR:')
    
    return float(input('ป้อนR:'))

#calAreaCircle
def calAreaCircle(r):
    #area = math.pi * r ** 2
    #area = math.pi * r * 2
    area = math.pi * math.pow(r,2)
    #return area
    return math.pi * math.pow(r,2)


#calRoundCircle 2 * pi * r
def calRoundCircle(r):
    #round = 2 + math.pi * r
    return 2 * math.pi * r


#ca;CubeCricle 4 / 3 * pi * r * r * r 
def calCubecircle(r):
    #cube = 4 / 3 * math.pi * r * r * r
    return 4 / 3 * math.pi * r * r * r


#showResult ชอทั้งหมดทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น ???? เส้นรอบวงเป็น ???? ปริมาตรทรงกลมเป็น ???? (^_-)เป้น(-_^)
def showResult():
    radius = inputRadius()
    area = calAreaCircle(radius)
    parameter = calRoundCircle(radius)
    volume = calCubecircle(radius)
    print('Redius:''%.4r' % radius)
    print('Area:''%.4r' % area)
    print('Parameter:''%.4r' % parameter)
    print('Volume:''%.4r' % volume)
    
    showResult()