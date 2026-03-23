class CourseResult:
    def __init__(self,course_code,mark):
        self.course_code=course_code
        self.mark=mark
        
    def grade_point(self):
        if self.mark >= 80:
            return 5.0
        elif self.mark >=70:
            return 4.0
        elif self.mark>=60:
            return 3.0
        elif self.mark >=50:
            return 2.0
        else:
            return 1.0
            
class Student:
    def __init__(self, name ,reg_no, student_no, results ):
        self.name=name
        self.reg_no=reg_no
        self.student_no=student_no
        self.results={}#adictionary mapping course_code to CourseResult
        
    def add_result(self, course_code,mark):
        Allowed_course_codes=["CSC1200","CSC1201","CSC1202","CSC1203","CSC1204"]
        if course_code in Allowed_course_codes:
            self.results[course_code]=CourseResult(course_code,mark)# for CourseResult we call the whole class
        else:
            print(f"{course_code} is not allowed")
    def compute_gpa(self):
        if not self.results:
            return 0.0
        else:
            total=sum (r.grade_point() for r in self.results.values())
            return total/len(self.results)
    
stud1=CourseResult("CSC1200",70)
stud2=CourseResult("CSC1201",80)
stud3=CourseResult("CSC1202",90)
stud4=CourseResult("CSC1203",75)
student1=Student("kakooza","25/u/03390/EVE",2500703390,{"CSC1200":99})

print("stud1=",stud1.course_code,stud1.grade_point() )
print("stud2=",stud2.course_code,stud2.grade_point() )
print("stud3=",stud3.course_code,stud3.grade_point() )
print("stud4=",stud4.course_code,stud4.grade_point() )
(student1.add_result("CSC1200",79))
(student1.add_result("CSC1201",71))
(student1.add_result("CSC1202",81))
(student1.add_result("CSC1203",90))
(student1.add_result("CSC1204",70))
print(student1.compute_gpa())