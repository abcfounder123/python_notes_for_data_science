
"""
Abstraction 

Abstract based class (ABC)
1. abstract method
2. abstract method

#################################################


from abc import ABC, abstractmethod


class CarRule(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def brake(self):
        pass


class AICarRule(ABC):
    @abstractmethod
    def gps(self):
        pass

    @abstractmethod
    def sensor(self):
        pass

    @abstractmethod
    def ai_control(self):
        pass


class CityCar(CarRule):
    def __init__(self):
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")

    def brake(self):
        print("brake")


class AICar(CarRule, AICarRule):
    def __init__(self):
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")

    def brake(self):
        print("brake")

    def gps(self):
        print("GPS .... ")

    def sensor(self):
        print("Sensor .... ")

    def ai_control(self):
        print("Control .... ")


#################################################

Polymorphism (interface)

1 2 3
Y G R       
G R Y      
R Y G      

#################################################

Summary

OOP concepts
1. Inheritance  (parent and child) (code reuse)
2. Composition  (friends)          (flexiable)
3. Polymorphism (easy user interface)
4. Encapsulation
5. Abstraction 

Core programming
- Custom Types
- Controlling by magic methods

#################################################

Design pattern (23)
1. Iterator pattern
2. Singleton pattern
...
...


Algorithms (1000, 300, 50)
Searching Algorithms
1. linearsearch   
2. binarysearch

#################################################

Exercises for 4 months

1. Tac Ti Toe                     =>  Procedural programming
2. Attributes 10 + 1              =>  OOP basics
3. Custom data types 11           =>  Core programming
4. Inheritance  30                =>  Large scale project
5. Inheritance and Composition 1  =>  ---

##################################################################################################

"""
