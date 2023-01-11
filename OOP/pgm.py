class Str:
    list = [23, 45, 67, 78]

class my_String (Str):

    def append(self, new):
        self.list.append(new)
        print("List after append",self.list)

    def pop(self, new):
        self.list.pop(new)
        print("list after pop",self.list)

a = Str
a = my_String()
a.append(85)
a.pop(2)


