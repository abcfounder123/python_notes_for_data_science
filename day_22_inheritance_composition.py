
"""

"Inheritance and Composition"

Inheritance

                             F

                         /   |   \\

                        A    T      O


A is a child class of F.  (parent and child)
A is a F.
T is a F.
O is a F.                 ('is a' relation)

#################################################

Diesel_Engine_Car
Petrol_Engine_Car
Car

#################################################

Diesel_Engine_Car is a Car. 
Petrol_Engine_Car is a Car. 

#################################################      

                        Car

                    /       \\

     Diesel_Engine_Car       Petrol_Engine_Car 

#################################################

Attributes

brand = "BMW"
serial_no = 0001

on()
off()

#################################################

1. Normal code


class Diesel_Engine_Car:
    def __init__(self, brand, serial_no):
        self.brand = brand
        self. serial_no = serial_no

    def on(self):
        print("Diesel Engine On.(more electric)")

    def off(self):
        print("Off.")


class Petrol_Engine_Car:
    def __init__(self, brand, serial_no):
        self.brand = brand
        self.serial_no = serial_no

    def on(self):
        print("Petrol Engine On.(less electric)")

    def off(self):
        print("Off.")

#################################################

2. Normal code to resuable code


class Car:
    def __init__(self, brand, serial_no):
        self.brand = brand
        self. serial_no = serial_no

    def off(self):
        print("Off.")


class Diesel_Engine_Car(Car):
    def on(self):
        print("Diesel Engine On.(more electric)")


class Petrol_Engine_Car(Car):
    def on(self):
        print("Petrol Engine On.(less electric)")



car1 = Diesel_Engine_Car(brand="BMW", serial_no="BMW-0001")
car2 = Petrol_Engine_Car(brand="Toyota", serial_no="Toyota-0001")

car1.on()
car1.off()

#################################################

{'brand': 'BMW', 'serial_no': 'BMW-0001'}
{'brand': 'Toyota', 'serial_no': 'Toyota-0001'}

Diesel Engine On.(more electric)
Petrol Engine On.(less electric)

##################################################################################################

Composition

Car has an Engine.
Car has a brand.
Car has a serial_no.

             Engine
         /
  Car    ---   brand
         \
            serial_no

#################################################

3. Normal code to flexible code      


class Car:
    def __init__(self, engine, brand, serial_no):
        self.engine = engine
        self.brand = brand
        self.serial_no = serial_no


#################################################


class DieselEngine:
    def on(self):
        print("Diesel Engine On.(more electric)")

    def off(self):
        print("Off.")


class PetrolEngine:
    def on(self):
        print("Petrol Engine On.(less electric)")

    def off(self):
        print("Off.")


class Car:
    def __init__(self, engine, brand, serial_no):
        self.engine = engine
        self.brand = brand
        self.serial_no = serial_no


car1 = Car(engine=DieselEngine(), brand="BMW", serial_no="BMW-0001")
print(car1.__dict__)
car1.engine.on()


car1.engine = PetrolEngine()   # flexible engine
print(car1.__dict__)
car1.engine.on()

#################################################

{'engine': Diesel_Engine object, 'brand': 'BMW', 'serial_no': 'BMW-0001'}
{'engine': Petrol_Engine object, 'brand': 'BMW', 'serial_no': 'BMW-0001'}

#################################################

Inheritance and Composition

1. Inheritance 

"Code reuse for large scale project"

AI car model.1 =>  parmanent          
AI car model.2 =>  parmanent          
AI car model.3 =>  parmanent         
AI car model.4 =>  parmanent

code lines = 400000

AI car model.1 is a Car.
AI car model.2 is a Car.
model.3 is a "model.1 + model.2".
model.4 is a model.3.               2

           Car               50000

        /      \\

model.1          model.2       50000,  50000

      \\       /

        model.3               150000,  0

          |

        model.4              200000,  50000


        200000
        550000

#################################################

Composition 

"Creating flexible code"

Car has various engines, various brake and various AI model

             Engine
         /
    Car   ---  brake
         \\
             AI model


m1
m2

Car(modal=m1)

#################################################

Drawing diagram for Inheritance and Composition

DieselEngineCar is a Car.    
PetrolEngineCar is a Car. 

                                Car

                             /        \\   

                         DC              PC

-------------------------------------------------

Car has an Engine.

Car  ---  Engine

-------------------------------------------------

DieselEngine is an Engine. 
PetrolEngine is an Engine. 

                          Engine

                       /         \\

                     D               P

-------------------------------------------------

"Sample code of Composition and Inheritance"


class Engine:
    def off(self):
        print("Off.")


class DieselEngine(Engine):
    def on(self):
        print("Diesel Engine On.(more electric)")


class PetrolEngine(Engine):
    def on(self):
        print("Petrol Engine On.(less electric)")


class Car:
    def __init__(self, engine, brand, serial_no, ai_model=None):
        self.engine = engine
        self.brand = brand
        self.serial_no = serial_no
        self.ai_model = ai_model


car1 = Car(engine=DieselEngine(), brand="BMW", serial_no="BMW-0001")
print(car1.__dict__)

car1.engine = PetrolEngine()
print(car1.__dict__)


##################################################################################################

Exercise of Composition and Inheritance

- Write code for the following pictures.


           Engine
         /
    Car   ---  brake
         \\
             AI model


                      Engine                             Brake

                    /        \\                        /       \

      DieselEngine             PetrolEngine       Normal          ABS


         AI model

        /      \\

model.1          model.2 

      \\       /

        model.3

          |

        model.4  


class Car:
    def __init__(self, engine, brake, ai_model):
        self.engine = engine
        self.brake = brake
        self.ai_model = ai_model


class Engine:
    pass

class DieselEngine(Engine):
    pass

class PetrolEngine(Engine):
    pass


class Brake:
    pass

class Normal(Brake):
    pass

class Abs(Brake):
    pass


class AiModel:
    pass

class Model1(AiModel):
    pass

class Model2(AiModel):
    pass

class Model3(Model1, Model2):
    pass

class Model4(Model3):
    pass


##################################################################################################

"""
