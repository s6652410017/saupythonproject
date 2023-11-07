# ลบไฟล์
import os
from os import remove

if os.path.exists('Myfile02.txt') :
    # os.remove('Myfile02.txt')
    remove('Myfile02.txt')
    print('ลบไฟล์เรียบร้อยแล้ว')
else :
    print('ไฟล์ที่จะลบไม่มี')