# OOP
# Camel case / Pascal case, Snake case
class Dtisau : 
    #data/property member ค่าช้อมูล
    stu_name = ''
    score = 0 
    gpa = 0


    #method member คือการทำงาน
    def histudent(self) :
        print(f'สวัสดี {self,stu_name}')

    def showScoreAndGrade(self) :
        print(f'คะแนน{self.score} ได้เกรด {self.gpa}')

# สร้าง object
obj01 = Dtisau() # 
obj02 = Dtisau()

obj01.stu_name = 'สมฃาย'
obj01.histudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = 'A'
obj02.histudent()
obj02.showScoreAndGrade()