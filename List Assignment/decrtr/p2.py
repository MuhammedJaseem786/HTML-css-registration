class OverloadingExample :
    def add (self, a, b):
        print(a+b)
    #def add(self,a,b,c):
       # print(a+b+c)

a=OverloadingExample()
a.add(5,10)
#a.add(5,10,20)