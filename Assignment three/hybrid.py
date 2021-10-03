class parent:
     def func1(self):
         print("This function is in parent.")

class childone(parent):
     def func2(self):
         print("This function is in childone. ")

class childtwo(parent):
     def func3(self):
         print("This function is in childtwo.")

class childthree(childone,parent):
     def func4(self):
         print("This function is in child three.")

object = childthree()
object.func1()
object.func2()
object.func4()
