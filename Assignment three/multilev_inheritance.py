class ParentClass:

    def feature_1(self,name):
        print('parent name is ',name)

class ChildClass_1(ParentClass):

    def feature_2(self,childone):
        print('child one name is ',childone)


class ChildClass_2(ChildClass_1):

    def feature_3(self,childtwo):
        print('child two name is ',childtwo)

obj = ChildClass_2()
obj.feature_1("john")
obj.feature_2("ram")
obj.feature_3("raju")
