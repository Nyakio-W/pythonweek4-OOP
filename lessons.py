#class attributes
#class person:
 #   pass

class Person:
    name = 'Skinny'

details = Person()
print(details.name)

#constructor
class Person:

    def __init__(self): # constructor method

        print('Constructor invoked')
details1 = Person()
details2 = Person()

#instance attributes
class Person:

    nationality = 'Ethiopian' # class attribute

    def __init__(self): # constructor

        self.name = '' # instance attribute

        self.age = 0 # instance attribute


#You can set the value of attributes using the dot notation, as shown below.

p1 = Person()

print(p1.name)
print(p1.age)
p1.name = "Mutemi" # assign value to instance attribute
p1.age = 65    # assign value to instance attribute

print(p1.name)  # access instance attribute value


print(p1.age)   # access value to instance attribute


class Person:

    def __init__(self, name, age): # class constructor

        self.name = name 

        self.age = age 

    def displayInfo(self): # class method

        print('Person Name: ', self.name,', Age: ', self.age)
p1 = Person('Mutemi', 65)

p1.displayInfo()

class Person:

    def __init__(self, name="mkuu", age=101):

        self.name=name

        self.age=age
p1 = Person()
print(p1.name)
print(p1.age)

#INHERITANCE IN PYTHON
#single inheritance
class Vehicle:
    def Vehicle_info(self):
        print('inside parent(vehicle) class')

class Car(Vehicle):
    def car_info(self):
        print('inside child(Car) class')

car = Car()
car.Vehicle_info()
car.car_info

#multiple inheritance
class Person:
    def person_info(self, name, age):
        print('inside person class')
        print('name:',name,'Age:',age)
class Company:
    def company_info(self, company_name, location):
        print('inside comany class')
        print('name:',company_name, 'location:',location)

class Employee(Person, Company):
    def Employee_info(self, salary,skill):
        print('inside employee class')
        print('salary:',salary,'skill:',skill)

emp = Employee()
emp.person_info('jessa',28)
emp.company_info('google','atlanta')
emp.Employee_info(1200,',machine learning')

#multilevel inheritance
# Base class
class Vehicle:
     def Vehicle_info( self):
         print( 'Inside Vehicle class')
# Child class
class Car(Vehicle):
    def car_info(self):
        print( 'Inside Car class')
# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')
# Create object of SportsCan
s_car = SportsCar()
# access Vehicle's and Car info using SportsCar object
s_car. Vehicle_info()
s_car. car_info()
s_car.sports_car_info()


#hierarchial inheritance
class Vehicle:
    def info(self):
        print( "This is Vehicle")
class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)
class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)
obj1 = Car()
obj1. info()
obj1. car_info( 'BMW')

obj2 = Truck()
obj2. info()
obj2. truck_info( 'Ford')


#hybrid inheritance
class Vehicle:
    def vehicle_info(self):
        print( "Inside Vehicle class" )
class Car(Vehicle):
    def car_info(self):
        print ("Inside Car class")
class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")
# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")
# create object
s_car = SportsCar()
s_car. vehicle_info()
s_car. car_info()
s_car. sports_car_info()

#python super function
class Company:
    def company_name(self):
        return 'Google'
class Employee(Company):
    def info(self):
# Calling the superclass method using super( )function
        c_name = Company.company_name(self)
        print("Jessa works at", c_name)
# Creating object of child class
emp = Employee()
emp.info()




#PYTHON ACCESS MODIFIERS
#public is just the normal way
#private members
class Parent:
    def __init__(self):
        self._protected_var = 20  # Protected variable
        self.__private_var = 30    # Private variable

class Child(Parent):
    def access_parent_vars(self):
        # Accessing the protected variable from the parent class
        print("Protected variable from parent:", self._protected_var)

        # Accessing the private variable from the parent class
        # This will raise an AttributeError because private variables cannot be accessed from subclasses
        print("Private variable from parent:", self.__private_var)

# Creating an object of the child class
child_obj = Child()
child_obj.access_parent_vars()


