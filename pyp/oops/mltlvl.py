class Grandfather:
    def OwnHouse(self):
        print("Grandpa House")
class Father(Grandfather):
    def OwnBike(self):
        print("Fathers bike")
class son(Father):
    def Ownbook(self):
        print("son have a book")
A = son()
A.OwnHouse()
A.OwnBike()
A.Ownbook()

#multiple

class Employee1():
    def __init__ (self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

class Employee2():
    def __init__ (self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class childemployee(employee1,employee2):
    def __init__ (self, name, age, salary, id)
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id
emp1 = Employee1("jaseem",21,1234)
emp2= Employee2("akbar",23,2345)













