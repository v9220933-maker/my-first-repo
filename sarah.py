class Person:
    def __init__(self,name,age):
	    self.name=name
		self.age=age
	def greet(self)
	    print(f"Hello {self.name}")

class Teacher(Person)
    def __init__(self,name,age,subject):
	    super().__init(name,age)
		self.subject=subject
	def teach(subject):
	    print(f"Mr/Ms {self.name} is teaching {self.subject}")
t1=Teacher("john",40,"mathematics")
t1.greet()
t1.teach()
