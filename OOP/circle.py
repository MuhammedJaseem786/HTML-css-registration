class Circle:
    def __init__(self,a,b,r):

        self.a = a
        self.b = b
        self.r = r
    def Area(self):
        print(self.r**2 * 3.14)

    def Perimeter(self):
        print(2* 3.14 *self.r)
    def testBelongs(self,x,y):
        if ((x - self.a) + (x - self.b) + (y - self.a) + (y - self.b) < (self.r ** 2)):
            return True
        else:
            return False
C = Circle(4,5,7)
C.Area()
C.Perimeter()
x = 10
y = 1
if C.testBelongs(x,y):
    print("Inside")
else:
    print("Outside")