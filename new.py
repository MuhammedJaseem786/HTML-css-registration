class cars:
    def intro1(self):
        print ("there are multiple types of cars in the world")
    def flight1(self):
        print ("there are different size of cars")

class innova1(cars):
    def flight(self):
        print ("this is a big car")

class nano1(cars):
    def flight(self):
        print ("this is small car")

obj_cars = cars()
obj_innova1 = innova1()
obj_nano1 = nano1()

obj_cars.intro1()
obj_cars.flight1()

obj_innova1.intro1()
obj_innova1.flight1()

obj_nano1.intro1()
obj_nano1.flight1()
