"""
class House:
    def __init__(self):
        self.street = ""
        self.stories = ""
        self.sqft = ""
        self.price = ""
        self.hasGarage = ""
        pass
house1 = House()
house1.hasGarage = True
house1.street = "Richmond Ave"
house1.stories = 3
house1.sqft = 3000
house1.price = 750000

print(vars(house1))


class Square:
    def __init__(self,length):
        self.length = length
        self.color = ""

sq = Square(5)
sq.color = "red"
print(vars(sq))




class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.area = width*height
re = Rectangle(5,3)

print(vars(re))
print("*******************************")


class Car:
    def __init__(self): # <---- initializer or constructor. has to be called in order to construct an object. i.e. 'Car'
        #properties of Car class
        self.make = ''
        self.model = ''
        self.color = ''
        self.speed = 0.0
    def accelerate(self):
        print("CAR SO FAST")
        self.speed += 10.0 
    def brake(self):
        self.speed -= 10.0    
        pass

car = Car() 

print(car)
car.make = 'Honda'
print(car.make)

print(f'Current speed: {car.speed}')
car.accelerate()
print(f'Current speed: {car.speed}')


class ShoppingList:
    def __init__(self,name):
        self.name = name
        self.grocery_items = []
class GroceryItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

sl = ShoppingList("Walmart")
print("print items in shopping list: ")
print(len(sl.grocery_items))

gi = GroceryItem("milk",3,1)

sl.grocery_items.append(gi)
print(len(sl.grocery_items))
"""

class Animal:
    def __init__(self):
        self.name = ""
    def eat(self):
        print("Animal is Eating!")
    def sleep(self):
        print("sleeping")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.name = ""
        self.tag_number = ""
        self.breed = ""        

cat = Cat()
cat.sleep()