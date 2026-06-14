"""
Answers of Attribute Exercises 

Step.1   --->   Write

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)

Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။  (size, pressure=0) ( pump(p) )
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။  (fuel_type, state="off") 
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

#################################################

Step.2   --->   Divide

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->  Tires
data    --->  size, pressure = 0
method  --->  pump(p)

class   --->  Engine
data    --->  fuel_type, state = off
method  --->  on(), off()

#################################################

Step.3   --->   Draw


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        pass


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        pass

    def off(self):
        pass
          

#################################################

Step.4   --->   controlling data by fun 

1. pressure by pump()  
   >> self.pressure = x
   
2. state by on() and off() 
   >> self.state = "on"
   >> self.state = "off"
        
        
class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print("ON")
        self.state = "on"

    def off(self):
        print("OFF")
        self.state = "off"
        
        
#################################################

Step.5   --->   controlling function by data 

on() and off() by state

if off: on
if on: off


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")
            

#################################################

Step.6   --->   Auto create serial number

n = 0

Car.n += 1
self.VIN = f"BMW-{Car.n:0>4}"


class Car:
    n = 0
    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")
            

#################################################

Step.7   --->   Controlling str value (Memory address to Car No)

<__main__.Car object at 0x104657cb0>      =>  BMW-0001(petrol engine(on))
<__main__.Tires object at 0x1004f35f0>    =>  15 inches tires
<__main__.Engine object at 0x10278f680>   =>  petrol engine(on)

def __str__(self):
    return f"<__main__.Car object at {hex(id(self))}>"
    
def __str__(self):
    return f"{self.VIN}({self.engine})"
    
def __str__(self):
    return f"{self.size} inches tires"

def __str__(self):
    return  f"{self.fuel_type} engine({self.state})"
    
    
class Car:
    n = 0
    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine
        
    def __str__(self):
        return f"{self.VIN}({self.engine})"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x

    def __str__(self):
        return f"{self.size} inches tires"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")

    def __str__(self):
        return f"{self.fuel_type} engine({self.state})"
    
        
#################################################    

Step.8   --->   Controlling representation str value (Memory address to Car No)

<__main__.Car object at 0x104657cb0>      =>  BMW-0001(petrol engine(on))
<__main__.Tires object at 0x1004f35f0>    =>  15 inches tires
<__main__.Engine object at 0x10278f680>   =>  petrol engine(on)

def __repr__(self):
    return f"{self.VIN}({self.engine})" 
    
def __repr__(self):
    return f"{self.size} inches tires"

def __repr__(self):
    return f"{self.fuel_type} engine({self.state})"    


class Car:
    n = 0
    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine
        
    def __repr__(self):
        return f"{self.VIN}({self.engine})"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x

    def __repr__(self):
        return f"{self.size} inches tires"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")

    def __repr__(self):
        return f"{self.fuel_type} engine({self.state})"
    

################################################# 

Step.9   --->   Creating many object


class Car:
    n = 0

    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine

    def __repr__(self):
        return f"{self.VIN}({self.engine})"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x

    def __repr__(self):
        return f"{self.size} inches tires"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")

    def __repr__(self):
        return f"{self.fuel_type} engine({self.state})"


cars = []

for _ in range(100):
    cars.append(Car(Tires(15), Engine("Gas")))

print(cars)

#################################################

Step.10   --->   Controlling many object


class Car:
    n = 0

    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine

    def __repr__(self):
        return f"{self.VIN}({self.engine})"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x

    def __repr__(self):
        return f"{self.size} inches tires"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")

    def __repr__(self):
        return f"{self.fuel_type} engine({self.state})"


cars = []

for _ in range(100):
    cars.append(Car(Tires(15), Engine("Gas")))

print(cars)

for car in cars[-10:]:
    car.engine.on()
 
print(cars)

#################################################

Step.11   --->   Reverse engineering


class Car:
    n = 0

    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine

    def __repr__(self):
        return f"{self.VIN}({self.engine})"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x

    def __repr__(self):
        return f"{self.size} inches tires"


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("ON")
            self.state = "on"
        else:
            print("already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("already off.")

    def __repr__(self):
        return f"{self.fuel_type} engine({self.state})"


cars = []

for _ in range(100):
    cars.append(Car(Tires(15), Engine("Gas")))

print(cars)

for car in cars[-10:]:
    car.engine.on()

print(cars)

##################################################################################################
##################################################################################################

"""

