class Car:
    def __init__(self,colour,name):
        self._colour=colour
        self._name=name
    def getter_name(self):
        return self._name
    def details(self):
        print(f"I am  a {self._name} and my clour is {self._colour}")
    def move_forward(self):
        print(f"{self._name} am moving forward now")
    def move_backward(self):
        print(f"{self._name} am moving backwards now")
    def stop(self):
        print(f"{self._name} has stopped")
class Motors(Car):
    def __init__(self, colour,name,brand):
        super().__init__(colour,name)
        self._brand=brand
    def action_4(self,number_plate):
        print(f"my brand is {self._brand} OF licence number {number_plate}")
    def move_backward(self):
        print(f"{self._name} am moivng backwards in the motor class")     
car1=Car("blue","toyota")
car2=Car("red","rumion")
car3=Car("black","land cruiser")
motor1=Motors("green","hilux","toyota")
cars=[car1,car2,car3]
for car in cars:
    car.details()
car1.move_forward()
motor1.move_backward()
motor1.action_4("uA 001D")
motor1.move_backward()
car2.move_backward()
print(car1.getter_name())
