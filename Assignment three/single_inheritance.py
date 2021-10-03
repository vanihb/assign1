class ParentClass:

    def char_1(self,name):
        print('parent name is',name)

    def char_2(self,eye):
        print('eyes are',eye)


class ChildClass(ParentClass):

    def char_3(self,myname):
        print('child name is',myname)

obj = ChildClass()
obj.char_1("john")
obj.char_2("same")
obj.char_3("ramjohn")
