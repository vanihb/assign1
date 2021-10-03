class Parent:
      def func1(self,name):
          print("This function is in parent class.",name)

class Child1(Parent):
      def func2(self,childone):
          print("This function is in child 1.",childone)
class Child2(Parent):
      def func3(self,childtwo):
          print("This function is in child 2.",childtwo)

object1 = Child1()
object2 = Child2()
object1.func1("john")
object1.func2("ram")
object2.func1("smita")
object2.func3("raju")
