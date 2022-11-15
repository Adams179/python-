


print("store management system")



#item1 = "phone"
#item1_price = 300000-
#item1_quantity = 100

#print(type(item1))
#print(type(item1_price))
#print(type(item1_quantity))

class item:
    pass
    #adding behaviour to the object
    def __int__(self):
        print("hey i have been created!")


    def calculate_discount(self,x, y):
        return x *  y

         





phone = item()
phone.name = "itel6"
phone.version = "android12"
phone.price = 2000

print(phone.name)
print(phone.price)


#calling the metbodes of class
print(phone.calculate_discount(0.8, phone.price))