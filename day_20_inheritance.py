
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

16. X ၏ attributes ကို ရှာဖွေပါက မည့်သည့်အစီအစဉ်အတိုင်း ရှာဖွေမည်နည်း။

                 
               Y          Z

             /  \\     /  |  \\    

             A    B    C   D   E   F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X                         

Method Resolution Order = X ->  A -> B -> Y  -> C -> D -> E -> Z  -> F


class Y:
    a = "Y"
    pass
class Z:
    a = "Z"
    pass

class A(Y):
    a = "A"
    pass
class B(Y):
    a = "B"
    pass

class C(Z):
    a = "C"
    pass
class D(Z):
    a = "D"
    pass
class E(Z):
    a = "E"
    pass

class F:
    a = "F"
    pass

class X(A, B, C, D, E, F):
    a = "X"
    pass


print(X.a) # X

#################################################

17. Method Resolution Order Exercise.1  => X BAY CDEZ F

               Y         Z

             /  \\    /  |  \\

             B   A   C   D   E    F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X      


class X(B, A, C, D, E, F):
    pass

#################################################

18. Method Resolution Order Exercise.2  => X CDEZ ABY F 

                Z             Y   

             /  |  \\        / \

            C   D     E     A   B   F

             \\   \\   |   /  /  /

                  \\ \\| / / /

                       X


class X(C, D, E, A, B, F):
    pass


#################################################

19. Method Resolution Order Exercise.3  => X F CDEZ ABY

                 Z             Y   

              /  |  \\        / \

       F    C    D     E     A   B  

         \\    \\   \\   |   /  /  

              \\   \\ \\| / / 

                       X

class Y:
    a = "Y"
    pass
class Z:
    a = "Z"
    pass

class A(Y):
    a = "A"
    pass
class B(Y):
    a = "B"
    pass

class C(Z):
    a = "C"
    pass
class D(Z):
    a = "D"
    pass
class E(Z):
    a = "E"
    pass

class F:
    a = "F"
    pass


class X(F, C, D, E, A, B):
    a = "X"
    pass


print(X.__mro__)

#################################################

20. Method Resolution Order Exercise.4  

=> Cross diamond example
=> X  A C BY DEZ F                            


                 Y       Z

               /    X    |  \\

              A   C   B  D   E    F

               \\   \\  |  /  /  /

                  \\ \\ | / / /

                        X       


class X(A, C, B, D, E, F):
    pass


#################################################

Diamond problem 
စိန်ပုံစံပျက်စီးလို့ ဖြစ်လာသော ပြဿနာ

consistent MRO
တစ်ခုကို တစ်ခါစီရှာရင် မှန်ကန်သော ရှာဖွေမှုပုံစံ

inconsistent MRO
တစ်ခုတည်းကို နှစ်ခါသုံးခါထပ်နေရင် မမှန်ကန်သော ရှာဖွေမှုပုံစံ

ပုံကို ကြည့်ပြီး စိန်ပုံစံမဖြစ်ရင် inconsistent MRO ဖြစ်နေကြောင်း အလွယ်တကူသိနိုင်။

"""
# A consistent method resolution order (MRO)

#                 Y

#            A   /\   B
#                \/

#                 X

# A, B သည် Y ဖြစ်သည်။
# X သည် A, B ဖြစ်သည်။  (A, B, Y)
"""

class X(A, B):
    pass


class X(Y, A, B):
    pass


"""
#################################################

# Not a consistent method resolution order

#                 Y
#              /

#          /    /   \
#              A      B
#          \    \   /
#            \
#              \
#                 X  


# X သည် Y, A, B ဖြစ်သည်။ (Diamond problem) (Y, A, B, Y)
# TypeError: Cannot create a consistent method resolution order (MRO)

#################################################  
"""

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


print(X.__mro__)

#################################################

21. Method Resolution Order Exercise.5 


               Y         Z

             /  \\    /  |  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X     

=> G is Y.
=> X is G.
=> X AGBY CDEZ F


Y
|
G      <---
|
X

               Y              Z

             /  | \\       /  |  \\

             A  G  B      C   D   E    F

               \\ \\  \\  |  /  /  /

                  \\ \\ \\| / / /

                         X       

class G(Y):
    pass


class X(A, G, B, C, D, E, F):
    pass


#################################################

22. Method Resolution Order Exercise.6 

                Y             Z

             /  | \\       /  |  \\

             A  G  B      C   D   E    F

               \\ \\  \\  |  /  /  /

                  \\ \\ \\| / / /

                         X     


=> H is Z.
=> X is H.
=> X AGBY CHDEZ F

Z
|
H    <---
|
X  

"""
#              Y              Z

#             / | \       / / | \

#             A G  B    C H  D   E   F

#               \ \ \   | | /  /  /

#                  \ \\ | |/ / /

#                        X

"""

class H(Z):
    pass


class X(A, G, B, C, H, D, E, F):
    pass


#################################################

23. Method Resolution Order Exercise.7  

=> X is I.
=> X AGBY CHDEZ F I

  I
  |
  X


"""
#              Y              Z

#             / | \       / / | \

#             A G  B    C H  D  E   F  I

#               \ \ \   | | /  /  / /

#                  \ \\ | |/ /  / /

#                        X


"""

class I:
    pass


class X(A, G, B, C, H, D, H, E, F, I):
    pass


#################################################

24. Method Resolution Order Exercise.8  

=> X is J.
=> X J AGBY CHDEZ F I

  J
  |
  X


"""
#              Y              Z

#             / | \       / / | \

#         J  A G  B     C H  D  E   F  I

#           \   \ \ \   | | /  /  / /

#               \  \ \\ | |/ /  / /

#                        X

"""

class J:
    pass


class X(J, A, G, B, C, H, D, E, Z, F, I):
    pass


#################################################

25. Method Resolution Order Exercise.9 

=> All is K.

               Y         Z

             /  \\    /  |  \\  

             A   B   C   D   E     F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X   

#################################################

=> All is K.

                     K


                /      \\   \\

               Y         Z

             /  \\    /  |  \\  \\

             A   B   C   D   E    F

               \\   \\ |  /  /  /

                  \\ \\| / / /

                       X   

#################################################

class K:
    a = "K"
    pass

class Y(K):
    pass
class Z(K):
    pass
class F(K):
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

print(X.a)

#################################################

Object Attributes (2)

1. Individual property, Object attribute, Instance attribute
2. Shared property, Class attribute, Static attribute

'property' refers to 'data & method'.
'attribute' refers to 'data & method'.

BMW-0001       <--- Individual
"BMW"          <--- Shared

ID             <--- Individual
Country name   <--- Shared

#################################################

name, age, ID                  50 + 50 + 50
country_name = "Myanmar"       1
precedence = "U BA"            1

1. Memory
total = 250 millions
total = 150 millions + 1 + 1

2. Flexiable

p1.country = "Burma"
p2.country = "Burma"
...
p50000000.country = "Burma"      <---  50

citizen.country = "Burma"        <---  1

#################################################

Object attributes နှစ်မျိုး

ပိုင်ဆိုင်မှုတွေ သတ်မှတ်ပေးတဲ့အခါ Oxygen ဘူးလိုမျိုးက တစ်ယောက်ချင်းစီကို အပိုင်ပေးလိုက်လို့ ရပါတယ်။

ဆေးရုံထဲက ပန်းခြံလိုမျိုးကြတော့ လူနာတစ်ယောက်ကို ပန်းခြံတစ်ခုဆိုတာမျိုး ပေးလို့ရပေမယ့် ဖြစ်နိုင်ရင် အတူတူမျှသုံးလိုက်ရင် အကုန်အကျပိုသက်သာပါတယ်။

ဒါကြောင့် object တွေကို Attributes တွေ ပေးတဲ့အခါ Oxygen ဘူးလိုမျိုး ကိုယ်ပိုင်ပစ္စည်းတွေ ရှိသလို ပန်းခြံလိုမျိုး ဘုံပိုင်ဆိုင်မှုတွေလည်း ရှိလာပါတယ်။

နှစ်မျိုးလုံးက object တွေနဲ့ သက်ဆိုင်တာဖြစ်လို့ object attributes လို့ပဲ ခေါ်ကြပါတယ်။

###########

သီခြားပိုင်ဆိုင်မှုတွေကို Individual Property တစ်နည်းအားဖြင့် Instance Attribute (instance variable) လို့ ခေါ်ပါတယ်။

ဘုံပိုင်ဆိုင်မှုတွေကိုတော့ Shared Property တစ်နည်းအားဖြင့် Class Attribute (static variable) လို့ ခေါ်ပါတယ်။

###########

Question .1 

Class attributes ဆိုတာက class ရဲ့ ပိုင်ဆိုင်မှုလား။
ဒါမှမဟုတ် object တွေရဲ့ ဘုံပိုင်ဆိုင်မှုလား။

Answer : Class level မှာ ရေးထားလို့သာ class attributes လို့ ခေါ်ပေမယ့် အဓိကရည်ရွယ်ချက်က memory သက်သာအောင် မျှသုံးနိုင်ဖို့ ဖြစ်ပါတယ်။

###########

Question.2

Car တစ်စီးမှာ brand အမျိုးအစားနဲ့  VIN number ဆိုတဲ့ ပိုင်ဆိုင်မှုနှစ်ခု ရှိတယ်ဆိုပါစို့။
ဘယ်ပိုင်ဆိုင်မှုကို မျှပြီး သုံးလို့ ရနိုင်မလဲ။

Answer : ဥပမာ Toyota ကုမ္ပဏီက ထုတ်တဲ့ကားတွေဆိုရင် ကားအစီးရေ ၁၀၀၀ ရှိပါစေ၊ အားလုံးရဲ့ Brand က "Toyota" ပဲ ဖြစ်မှာပါ။ အစီးတိုင်းအတွက် memory ထဲမှာ "Toyota" လို့ လိုက်ရေးနေမယ့်အစား Class Level မှာ တစ်ခါပဲ ရေးထားပြီး အားလုံးက မျှသုံးတာ ပိုထိရောက်ပါတယ်။

VIN ဆိုတာကြတော့ ကားတစ်စီးချင်းစီရဲ့ ကိုယ်ပိုင် မှတ်ပုံတင်နံပါတ် (စက်နံပါတ်) လိုမျိုးပါ။ ကားတစ်စီးနဲ့ တစ်စီး မတူနိုင်တာကြောင့်  Instance Attribute အဖြစ်ပဲ ထားရပါမယ်။

#################################################

26. What should be Class level data?

50 millions people

1. Name       -  obj    =>   500 millions   =>  500 MB
2. ID         -  obj    =>   500 millions   =>  500 MB
3. age        -  obj    =>   500 millions   =>  500 MB 
4. "Myanmar"  -  obj    =>   500 millions   =>  500 MB 
                                            +   2000 MB


1. Name       -  obj    =>   500 millions   =>  500 MB
2. ID         -  obj    =>   500 millions   =>  500 MB
3. age        -  obj    =>   500 millions   =>  500 MB 
4. "Myanmar"  -  cls           1            =>  100 bytes 

                                            +   1500 MB + 100 bytes 

#################################################

{'name': 'p1', 'id': '000000001', 'age': 20, 'country': 'Myanmar'}
{'name': 'p2', 'id': '000000002', 'age': 30, 'country': 'Myanmar'}


class X:
    def __init__(self, name, id, age, country):
        self.name = name
        self.id = id
        self.age = age 
        self.country = country


p1 = X(name="p1", id="000000001", age=20, country="Myanmar")
p2 = X(name="p2", id="000000002", age=30, country="Myanmar")

print(p1.__dict__)
print(p2.__dict__)

p1.country = "Burma"
p2.country = "Burma"

print(p1.__dict__)
print(p2.__dict__)

#################################################

{'name': 'p1', 'id': '000000001', 'age': 20}
{'name': 'p2', 'id': '000000002', 'age': 20}


class X:
    country = "Myanmar"  # class level data

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


p1 = X(name="p1", id="000000001", age=20)
p2 = X(name="p2", id="000000002", age=20)

print(p1.__dict__)
print(p2.__dict__)

print(p1.country)
print(p2.country)

X.country = "Burma"

print(p1.country)
print(p2.country)

#################################################

{'name': 'p1', 'id': '000000001', 'age': 20}         300 bytes
{'name': 'p2', 'id': '000000002', 'age': 20}         300 bytes

country = "Myanmar"  =>  100 bytes                   create once, less memory usage

X.country = "Burma"                                  update once, Flexiable

#################################################

27. Use inheritance for the following code.


class Male:
    gender = "male"
    country = "Myanmar"
    percedence = "U Ba"
    system = "Democracy"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Female:
    gender = "female"
    country = "Myanmar"
    percedence = "U Ba"
    system = "Democracy"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


#################################################


class X:
    country = "Myanmar"
    percedence = "U Ba"
    system = "Democracy"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Male(X):
    gender = "male"


class Female(X):
    gender = "female"


#################################################

p1 = Male(id="123456789", name="Mg Mg", age=20)
print(p1.gender)
print(p1.country)

#################################################

28. Create relations for the following classes.

Myanmar Human
Yangon Human
Mandalay Human
America Human
Newyork Human
Human

                                Human     head = 1
                            
                            /            \\
                            
                    Myanmar Human       America Human

                       /    \\                   \\
                       
                Yangon Human   Mandalay Human     Newyork Human


800 billions , 600 bytes, 100 bytes

obj, class level, inheritance

#################################################

29. Create relations for the following classes.

Car
Engine Car
Electric Car
Diesel Car
Petrol Car

                       Car

                    /       \\

           Engine Car         Electric Car

           /    \\

   Diesel Car     Petrol Car

#################################################

30. Draw MRO for the following relations.

A is a F.    (ပန်းသီး is a Fruit.)
T is a F.    (သစ်တော်သီး is a Fruit.)
O is a F.    (Orange is a Fruit.)

AT is a A.   (ပန်းသစ်တော်သီးသည် ပန်းသီးဖြစ်သည်။)
AT is a T.   (ပန်းသစ်တော်သီးသည် သစ်တော်သီးဖြစ်သည်။)
(ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။)

O1 is a O.
O2 is a O.
O3 is a O.
                             F

                         /   |   \\

                        A    T       O

                        \\   /    /  |  \\

                          AT     O1  O2   O3

#################################################

Knowledges                               

1. comma + space                              x = [1, 2, 3, 4]
2. operator => s + operator +  s              1 + 2
3. fun, class  => line 2
4. while, if, for  =>  line 1
5. normal program  =>  no line, line 1
6. class name => UpperCamealCase
7. all name => lower case, lower_snake_case
8. constant => UPPER CASE

9. Diamond problam (YAB => YABY)
10. MRO

##################################################################################################

"""
