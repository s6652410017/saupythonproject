def studentdetails():
    s_id = input("ID student : ")
    s_name = input("Name student : ")
    grade = float(input("Grade student : "))
    return s_name, s_id , grade

def gradecal(gradcheck):
    if gradcheck < 2.00 :
        return "ผ่าน"
    else :
        return "ไม่ผ่าน"
    
def showresult(s_id, s_name, result):
    print(f"รหัสนักเรียน: {s_id}")
    print(f"ชื่อนักเรียน: {s_name}")
    print(f"เกรดนักเรียน: {result}")

studentnumber = int(input("จำนวนนักเรียน : "))

for i in range(studentnumber):
    s_id, s_name, grade = studentdetails()
    result = gradecal(grade)
    showresult(s_id, s_name, result)