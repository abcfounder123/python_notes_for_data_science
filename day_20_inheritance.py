
"""

OOP
- Attributes
- Inheritance

#################################################

Inheritance
- parent and child 
- code reuse

#################################################

Types of inheritance
1. Single inheritance 
2. Multiple inheritance
3. Mutilevel inheritance 
4. Hierarchical inheritance
5. Hybrid inheritance

#################################################

1. Single inheritance

       Animal  

         |

        Dog


class Animal:
    def eat(self):
        print("Animal eat.")


class Dog:
    def eat(self):
        print("Animal eat.")

    def bark(self):
        print("Dog bark.")


#################################################


class Animal:
    def eat(self):
        print("Animal eat.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


x = Dog()
x.eat()
x.bark()

#################################################

2. Multiple inheritance  

          Father   Mother
             \\     /
               Child


      old.1  old.2  old.3  old.4  old.5  old.6  old.7    =>  700
      
          \\           |             /             /

                     New                                 => old 400   


class New(old.1, old.3, old.5, old.7):
    pass

#################################################

class Phone:
    def call(self, number):
        print("Calling to ", number)


class Camera:
    def take_photo(self):
        print("Taking a photo.")


class SmartPhone:
    def call(self, number):
        print("Calling to ", number)

    def take_photo(self):
        print("Taking a photo.")

#################################################

class Phone:
    def call(self, number):
        print("Calling to ", number)


class Camera:
    def take_photo(self):
        print("Taking aa photo.")


class SmartPhone(Phone, Camera):
    pass


y = Phone()
y.call("09123456")

z = Camera()
z.take_photo()

x = SmartPhone()
x.call("09123456")
x.take_photo()

#################################################

3. Mutilevel inheritance

          Grand X  
            |
         Parent Y       Single inheritance
            |
          Child Z       Mutilevel inheritance


class X:
    def x(self):
        print("x")


class Y(X):
    def y(self):
        print("y")


class Z(Y):
    def z(self):
        print("z")


a = Z()
a.z()
a.y()
a.x()


#################################################

4. Hierarchical inheritance


                        Human     
                     
                     /    |     \\
                    
                 white   Brown  Black



            X          eat .1

         /     \\

      Y           Z
     bark        meow



class Animal:
    def eat(self):
        print("Animal eat.")


class Dog:
    def eat(self):
        print("Animal eat.")

    def bark(self):
        print("Dog bark.")


class Cat:
    def eat(self):
        print("Animal eat.")

    def meow(self):
        print("Cat meow.")


#################################################

class Animal:
    def eat(self):
        print("Animal eat.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


class Cat(Animal):
    def meow(self):
        print("Cat meow.")

x = Dog()
x.eat()
x.bark()

#################################################

            X  

         /     \\

      Y           Z



class X:
    pass


class Y(X):
    pass


class Z(X):
    pass


#################################################

5. Hybrid inheritance

              A       Hierarchical inheritance

           /     \\

          B        C      single

           \\     /

               D      (multiple + multilevel) => Hybrid


D(B, C)            (multiple)
D <- B <- A        (multilevel)
D <- C <- A        (multilevel)


################################################################################################## 

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

class   =>   Laptop
data    =>   serial_no
method  =>   on(), off()

class Laptop:
    def __init__(self, n):
        self.serial_no = n

    def on(self):
        pass

    def off(self):
        pass

#################################################

2. Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

#################################################

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။


class   =>   DialUp
data    =>   speed = 9600bit/s
method  =>   download()

class DialUp:
    def __init__(self):
        self.speed = 9600bit/s

    def download(self):
        print(f"Download with {self.speed}.")

#################################################   

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။   (size, pressure, pump)
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

9. Engine တွင် fuel_type ပါသည်။     fuel_type, state, on(), off()  
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

10. Create a city car of 7 (from 8 and 9) and (pump 7 and on)

# city_car -> "BMW-0001", 15" tires, Petrol engine
# 7psi, on

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))
city_car.tires.pump(7)
city_car.engine.on()

#################################################

အရာဝတ္ထုတွေဟာ သီခြားစီဆိုပေမယ့် အလုပ်လုပ်တဲ့အခါမှာတော့ ပေါင်းစပ်ပြီး လုပ်ကြရပါတယ်။

programming မှာလည်း ဒီအယူအဆကို ယူသုံးထားပါတယ်။

ပေါင်းစပ်မှု ပုံစံနှစ်မျိုး

1. ခိုင်မြဲသော တွဲစပ်မှု (မိဘနဲ့ သားသမီးလိုမျိုး)
2. လျော့ရဲသော တွဲစပ်မှု (အသိမိတ်ဆွေလိုမျိုး)

Data အယူအဆအရဆိုရင်တော့ 'is a' relation နဲ့ 'has a' relation ဆိုပြီး ခေါ်ကြပါတယ်။
OOP အယူအဆအရဆိုရင်တော့ inheritance နဲ့ composition ဆိုပြီး ခေါ်ကြပါတယ်။

Tightly couple    =>  'is a', inheritance
Loosely couple    =>  'has a', composition

BMW is a Car.     =>  'is a', inheritance       BMW(Car)
BMW has a Tire.   =>  'has a', composition      self.tire = t

ခြေလက်လိုမျိုး အသေထားချင်ရင် tightly coupled.
အဝတ်အစားလိုမျိုး အလွယ်တကူ လဲလှယ်ချင်ရင် loosely coupled.

#################################################

class BMW(Car):        <---   inheritance 
    pass


class BMW(Car):
    def __init__(self, t):
        self.tire = t        <---   composition
        
#################################################

တကယ်‌တော့ has a relation မှာလည်း strong နဲ့ weak ဆိုပြီး နှစ်ခု ရှိပါသေးတယ်။

-------------------------------------------------

"Composition"

object ပျက်စီးတဲ့အခါ ပေါင်းစပ်ထားတာပါ ပျက်စီးခဲ့ရင် strong has a တစ်နည်းအားဖြင့် composition 

>> Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))

-------------------------------------------------

"Aggregation"

object ပျက်စီးတဲ့အခါ ပေါင်းစပ်ထားတာက ဆက်ပြီးရှိနေခဲ့ရင် weak has a တစ်နည်းအားဖြင့် aggregation

e1 = Engine("Petrol")
Car(VIN="BMW-0001", tires=Tires(15), engine=e1)

အလွယ်မှတ်ရရင် Engine ကို အပြင်မှာ သီးသန့်ဖန်တီးရင် weak ပေါ့။

#################################################

Composition / aggregation example (Loosely couple)

data တွေကို အသေမဟုတ်ပဲ ချိတ်ဆက်ချင်ရင် assignment operator သုံးရပါမယ်။


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine     # Car has an engine. "has a"


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, p):
        print(f"pump to {p} psi.")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        print(f"{self.fuel_type} Engine Off.")

    def __repr__(self):
        return f"{self.fuel_type} Engine"


# city_car -> "BMW-0001", 15" tires, Petrol engine
# 7psi, on

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=Engine("Petrol"))  # strong has a
print(city_car.engine)

city_car.engine = Engine("Gas")     # <---  Loosely couple (Engine ကို အလွယ်တကူ အသစ်လဲနိုင်ပါတယ်။)
print(city_car.engine)

-------------------------------------------------

e1 = Engine("Petrol")

city_car = Car(VIN="BMW-0001", tires=Tires(15), engine=e1) # weak has a
print(city_car.engine)

del city_car
print(e1)

##################################################################################################

Inheritance exercise

11. Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။
F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။ 

#################################################

F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။ ( is a relation ) (tightly coupled) (inheritance) 

F35 is a Jet.
F22 is a Jet.

       Jet
     /     \\
   F35     f22

#################################################

Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။

name     -->  Jet
data     -->  role, name, country
method   -->


class Jet:
    def __init__(self, role, name, country):
        self.role = role
        self.name = name
        self.country = country


# F35 သည် Jet လေယာဉ်ဖြစ်သည်။ is a,
class F35(Jet):
    pass

# F22 သည် Jet လေယာဉ်ဖြစ်သည်။
class F22(Jet):
    pass


x = F35("Multirole", "F35-001", "USA")

print(x.__dict__)

#################################################

                  Car

                /     \\

            BMW       TOYOTA

parent class, super class, base class
child class, sub class, derived class


ဝေမျှမှုပုံစံကို ရည်ညွှန်းချင်ရင် parent and child        A B

အုပ်စုခွဲတာကို ပေါ်လွင်စေချင်ရင် super and sub         4, 8, 

ဆင့်ပွားမှုပုံစံကို မြင်စေချင်ရင် base and derived        pt

#################################################

12.

I, J, K သည် A ၏ sub class ဖြစ်သည်။
X သည် I ၏ sub class ဖြစ်သည်။
Y သည် J ၏ sub class ဖြစ်သည်။
Z သည် K ၏ sub class ဖြစ်သည်။

ပုံဆွဲပါ။ class တည်ဆောက်ပါ။


I, J, K သည် A ၏ sub class ဖြစ်သည်။
A သည် I, J, K  ၏ super class ဖြစ်သည်။

               A

           /   |   \\

        I      J      K

X သည် I ၏ sub class ဖြစ်သည်။

            I

            |

            X

Y သည် J ၏ sub class ဖြစ်သည်။

            J

            |

            Y

Z သည် K ၏ sub class ဖြစ်သည်။

            K

            |

            Z


               A

           /   |   \\

        I      J      K

      /        |       \\

    X          Y         Z


class A:
    pass


class I(A):
    pass


class J(A):
    pass


class K(A):
    pass


class X(I):
    pass


class Y(J):
    pass


class Z(K):
    pass


#################################################

13.  အောက်ပါပုံအတိုင်း class တည်ဆောက်ပါ။


                      Fruit           

              /         |        \\

         Apple        Mango       Banana  

                  /     |     \\

             မချစ်စု   စိန်တလုံး   တောသရက်


class Fruit:
    pass


class Apple(Fruit):
    pass


class Mango(Fruit):
    pass


class Banana(Fruit):
    pass


class မချစ်စု(Mango):
    pass


class စိန်တလုံး(Mango):
    pass


class တောသရက်(Mango):
    pass


#################################################

multiple inheritance exercises

14. ပန်းသီးနှင့် သစ်တော်သီးသည် သစ်သီးများဖြစ်ကြသည်။ 

ပန်းသစ်တော်သီးသည် ပန်းသီးနှင့် သစ်တော်သီးနှစ်မျိုးလုံးမှ မျိုးဗီဇများ အမွေဆက်ခံထားသည်။

ထို့ကြောင့် ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။

ပုံဆွဲပြီး class တည်ဆောက်ပါ။


                       သစ်သီး

                     /        \\

                ပန်းသီး           သစ်တော်သီး

                    \\          /

                     ပန်းသစ်တော်သီး    


class သစ်သီး:
    pass


class ပန်းသီး(သစ်သီး):
    color = "white"
    pass


class သစ်တော်သီး(သစ်သီး):
    taste = "sweet"
    pass


class ပန်းသစ်တော်သီး(ပန်းသီး, သစ်တော်သီး):
    pass


x = ပန်းသစ်တော်သီး()
print(x.color)
print(x.taste)

#################################################

15.

A, B သည် Y ဖြစ်သည်။
C, D, E သည် Z ဖြစ်သည်။
X သည် A, B, C, D, E, F ဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။

#################################################


X သည် A, B, C, D, E, F ဖြစ်သည်။


A, B သည် Y ဖြစ်သည်။

                    Y

                 /     \\

               A           B


C, D, E သည် Z ဖြစ်သည်။               


                    Z

                 /   |  \\

               C     D     E


X သည် A, B, C, D, E, F ဖြစ်သည်။


               A    B   C   D   E   F

                \\   \\ |  /  /  /

                        X

#################################################

               Y          Z             

             /  \\     /  |  \\    

             A    B    C   D   E   F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X     

                       X  ABY CDEZ F



#                 Y

#            A   /\   B
#                \/

#                 X


class Y:
    pass
class Z:
    pass
class F:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class X(A, B, C, D, E, F):
    pass

print(X.__mro__)  # X  ABY CDEZ F


#################################################


"""
