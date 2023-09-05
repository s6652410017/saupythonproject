#คำนวนเงินที่จะแฃร์กัน ป้อนเงิน ฟ้อนคน และแสดงเงินที่จะแชร์กันทางหน่วยหน้าจอ
#โดยให้เขียนเป็นฟังก์ฃั่น อย่างน้อย 2 ฟังก์ฃั่น
#cast/conversation

#รับค่าช้อมูล
def inputMoneyPerson() :
    money = float( input('ป้อนเงิน :'))
    person = int (input ('ป้อนคน : '))
    return money, person

#คำนวณ และแสดงผล
def calAndShowMoneyShare(money, person) :
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์คนขอเป็นเลขจำนวณเต็มปัดขึ้น
    
    doublefloatmoney = '%.2f' % money
     
    print(f'จำนวนเงิน {money:.sf}  บาท  {person} คน แฃร์กันคนละ {round(money/person)} บาท ')
    print('จำนวนเงิน',('%.2f' % money),'บาท',person,'คน แชร์กันคนละ',round(money/person),'บาท')  
    print("จำนวนเงิน "+str("%.2f" % money) + "บาท" +str(person) +" คน แฃร์กันคนละ "+str(round(money/person)) + "บาท")
    print('จำนวนเงิน {} บาท {} คน แชร์กันคนละ {} บาท'.format(doublefloatmoney, person ,round(money/person)))  
    print('จำนวนเงิน %s บาท %d คน แชร์กันคนละ %d บาท' %(doublefloatmoney, person, round(money/person )))
     
    
money, person = inputMoneyPerson( )

calAndShowMoneyShare( money, person)