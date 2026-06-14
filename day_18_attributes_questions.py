
"""

Attribute Exercises  (1 to 11)

#################################################

Step.1   --->   Write
Step.2   --->   Divide                         20 seconds
Step.3   --->   Draw design                    45 seconds
Step.4   --->   controlling data by fun        15 seconds
Step.5   --->   controlling function by data   10 seconds
Step.6   --->   Auto create serial number      10 seconds
Step.7   --->   Controlling str value          20 seconds
Step.8   --->   Controlling repr value         20 seconds
Step.9   --->   Creating many object           15 seconds
Step.10  --->   Controlling many object        10 seconds

2 minutes 45 seconds
2 minutes

Step.11   --->   Reverse engineering           30 seconds

#################################################

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

Step.2   --->   Divide                        (20 seconds)

class   --->  
data    --->  
method  --->

class   --->  
data    --->  
method  --->

class   --->  
data    --->  
method  --->

#################################################

Step.3   --->   Draw                          (45 seconds)


class Car:
    def __init__(self):
      

class Tires:
    def __init__(self):
       

class Engine:
    def __init__(self):
          

#################################################

Step.4   --->   controlling data by fun       (15 seconds)

1. pressure by pump()  
   >> self.pressure = x
   
2. state by on() and off() 
   >> self.state = "on"
   >> self.state = "off"
        
#################################################

Step.5   --->   controlling function by data  (10 seconds)

on() and off() by state

if off: on
if on: off

#################################################

Step.6   --->   Auto create serial number     (10 seconds)

n = 0

Car.n += 1
self.VIN = f"BMW-{Car.n:0>4}"

#################################################

Step.7   --->   Controlling str value (Memory address to Car No)    (20 seconds)

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
        
#################################################    

Step.8   --->   Controlling representation str value      (20 seconds)

<__main__.Car object at 0x104657cb0>      =>  BMW-0001(petrol engine(on))
<__main__.Tires object at 0x1004f35f0>    =>  15 inches tires
<__main__.Engine object at 0x10278f680>   =>  petrol engine(on)

def __repr__(self):
    return f"{self.VIN}({self.engine})" 
    
def __repr__(self):
    return f"{self.size} inches tires"

def __repr__(self):
    return f"{self.fuel_type} engine({self.state})"    

################################################# 

Step.9   --->   Creating many object                      (15 seconds)

cars = []

for _ in range(100):
    cars.append(Car(Tires(15), Engine("Gas")))

#################################################

Step.10   --->   Controlling many object                  (10 seconds)

# last 10 on

for car in cars[-10:]:
    car.engine.on()
 
#################################################

Step.11   --->   Reverse engineering                      (30 seconds)

##################################################################################################


"""