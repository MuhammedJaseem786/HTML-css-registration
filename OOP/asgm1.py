class Rectangle:
  def _init_(self,len,wid):
    self.len=len
    self.wid=wid
  def perimeter(self):
    return 2*(self.len+self.wid)
  def area(self):
    return self.len*self.wid
  def display(self):
    print("Length is:",self.len,"Width is:",self.wid,"Perimeter is:",self.perimeter(),"Area is:",self.area())
class Parallelepiped(Rectangle):
  def _init_(self,len,wid,high):
    Rectangle._init_(self,len,wid)
    self.high=high
  def Volume(self):
    return self.len*self.wid*self.high
Rect= Rectangle(8,3)
Rect.display()
Para=Parallelepiped(7,5,3)
print('Volume is:',Para.Volume())
