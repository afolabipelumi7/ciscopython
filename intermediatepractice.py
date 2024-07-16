
try:
    age = int(input("age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")

except ValueError:
    print("invalid value")
#just used for printing proper error messages than making it crash

#classes #oop
number = [1,2,3]
class Point:
    def __init__(self,x,y):#innit used to construct or create an object
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")
#object
point = Point(10,20)
point.x = 11
print(point.x)
#point1.x = 10
#point1.y = 20
#print(point1.x)
#point1.draw()

#point2 = Point(10,20)#x and y cordinates
#point2.x = 1
#print(point2.x)



class Person:
    def __init__(self,name):
        self.name = name#self is used to access variables that belong to the class
    def talk(self):
        print(f"Hi,i am {self.name}")

john = Person("john smith")
print(john.name)
john.talk()

bob = Person("bob smith")
bob.talk()

#inheritance
class Mammal:
    def walk (self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

#dog1 = Dog()
#dog1.walk()

#cat1 = Cat()
#cat1.be_annoying()

#importing modules
#import converters
#print(converters.kg_to_lbs(70))


#importing specific modules
import converters
#from converters import kg_to_lbs
#kg_to_lbs(100)


#import pelumi
#from pelumi import findmax
#findmax()

#pakages

#importing packages
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce import shipping
shipping.calc_shipping()


#generating random values
import random
for i in range(3):
     print(random.randint(10,20))

member = ["john","mary","bob"]
leader =random.choice(member)
print(leader)


class Dice():
    def roll(self):
        for i in range(3):
            y = random.randint(1, 6)
            u = random.randint(1,6)
        print((y,u))



dice = Dice()
print(dice.roll())

#directories and file paths
from pathlib import Path
#absolute pass
#c:\program\microsoft  - windows
#relative pass

#path = Path("ecommerce")
#print(path.exists())
#return boolean

p = Path()
#print(p.mkdir()) #to make new directory

print(p.rmdir()) # to remove file path










