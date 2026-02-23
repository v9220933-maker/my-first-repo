class Student:
    def __init__(self,full_name,registration_number,student_number):
        self.full_name=full_name
        self.registration_number=registration_number
        self.student_number=student_number
        self.id_number=f"{student_number}-{registration_number}"
	
    def details(self):
        print(self.full_name)
        print(self.registration_number)
        print(self.student_number)
        print(self.id_number)
		
person1=Student("jv","25/U/03390",2500703390)
person1.details()
class CEDAT_student(Student):
    pass
class CoCIS_student(Student):
    pass
class EDUC_student(Student):
    pass
person2=CEDAT_student("KV","25/U/03391",2500703391)
person2.details()
class EASLIS_student(CoCIS_student):
    pass
class SCIT_student(CoCIS_student):
    pass
class CS_student(Student):
    pass
class SE_student(Student):
    pass