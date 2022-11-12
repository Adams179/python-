class Student:
      def __init__(self,regno,name,age):
            self.regno=regno
            self.name=name
            self.age=age

      def study (self):
            return "iam studying"
      def play (self):
        return "Iam playing"
      def Discuss (self):
        return "Iam Discussing"


class NetworkAdmin(Student):
    def __init__(self, regno, name, age):
        super().__init__(regno, name, age)
        


Student_2=NetworkAdmin("s21315","adams",32)

print(Student_2.study())



Student_1=Student("S21B13/047","Murungi",65)
print(Student_1)

print(Student_1.study())

print(Student_1.play())










