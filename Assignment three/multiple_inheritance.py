class ParentClass_one:

    def char_one(self,fname):
        print('father name is ',fname)

class ParentClass_two:

    def char_two(sel,mname):
        print('mother name is ',mname)


class ChildClass(ParentClass_one, ParentClass_two):

    def char_three(self,myname,eyes):
        print(myname," ",eyes)

obj = ChildClass()
obj.char_one("john")
obj.char_two("smita")
obj.char_three("ramjohn","same")
