class Student:
    _name = None
    _roll = None
    _course = None
    #constructor
    def __init__(self, name, roll, course):
        self._name = name
        self._roll = roll
        self._course = course
    #protected member function
    def _displayrollandbatch(self):#accessing protected data members
        print("Roll:",self._roll)
        print("Course:",self._course)

class myclass(Student):
     def init(self, name, roll, branch):
         Student.init(self, name, roll, branch)

     def displayDetails(self):
         pass

     print(self._name)
     self._displayrollandbatch()

obj = myclass("vishnu", 10, "python")
obj.displayDetails()
