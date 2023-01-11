class Student:
    school_name = 'ABC School'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print('student:', self.name, self.age, Student.school_name)

    def change_age(self, new_age):
        self.age = new_age

    @classmethod
    def modify_school_name(cls, new_name):
        cls.school_name = new_name

s1 = Student("Harry", 12)

s1.show()
s1.change_age(14)

Student.modify_school_name('XYZ School')

s1.show()