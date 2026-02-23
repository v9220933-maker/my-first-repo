class Person:
	def __init__(self,name,age):
        self.name=name
        self.age=age

	def greet(self):
        print(f"hello {self.name}")
	
class Teacher(Person):
	def __init__(self,name,age,subject):
        super().__init__(name,age)  
        self.subject=subject
	def teach(self):
        print(f"Mr/Ms {self.name} is teaching {self.subject}")
t1=Teacher("john",40,"mathematics")#creating an object for teacher.
t1.greet()
t1.teach()