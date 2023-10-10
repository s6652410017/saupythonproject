# คำสั่ง break กับ continue ที่มักใฃ้ร่วมกับ control flow
for x in range(5) :
    if x == 3 :
        break; # break ทำงานเมื่อไหร้จบ Loop ทันที
    print(f"SAU...{x}")
        
print('................')

for y in range(5) :
    if y == 3 :
        continue; # continue ทำงานเมื่อไหร่จะจบรอบนั้น ไปรอบต่อไปทันที
    print(f"DTI...{y}")