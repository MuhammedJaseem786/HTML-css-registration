class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def address(self):
        print(self.name, self.contact)

class doctor(Person):
    pass

class patient(Person):
    pass

pat = Person("Vishnu",234567)
doc = Person("Priya", 8521234)

pat.address()
doc.address()
