class student:

    def eat(self ):
        print("i am eating")

    def __init__(self,name,course,access_no):
        self.name = name
        self.course = course
        self.access_no = access_no
        #print(" hey i have come to life")

    def drink(self ):
        print("i am drinking")


    def sleep(self):
        print("i am sleeping")


    def eat( ):
        print("i am eating")   

    def __str__(self):
        return f"hey this is (self.name)"
           
#adams = student()
#print(adams.eat)

adams = student("murungi", "BSIT", "A94412")
print(adams.access_no)







