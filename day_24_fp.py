
"""

1. List Comprehension
ရှိပြီးသား list တစ်ခုကို အခြေခံပြီး list အသစ်တစ်ခုကို တိုတိုတုတ်တုတ်နဲ့ အလွယ်တကူ တည်ဆောက်တဲ့ နည်းလမ်းဖြစ်ပါတယ်။
ကြာချိန်က ပုံမှန် for loop ထက် ပိုမြန်ပါတယ်။
ရင်းနှီးသွားပြီဆိုရင် For loop ထက်လည်း ဖတ်ရလွယ်ပါတယ်။

-----------------------------------------

2. Decorator
မူရင်း function ကို တိုက်ရိုက်မပြင်ပဲ
ကြားခံ function တစ်ခုနဲ့  လုပ်ဆောင်ချက်အသစ်တွေ ထပ်ပေါင်းထည့်တာမျိုးပါ။
တတိယမြောက် function ကို ဘယ်လိုအမည်ပေးမလဲဆိုတာမျိုး သိရပါမယ်။

-----------------------------------------

3. Generator 
Data တွေကို တစ်ခါတည်း အကုန်မထုတ်ပေးဘဲ လိုအပ်တဲ့အချိန်မှ တစ်ခုချင်းစီ ထုတ်ပေးတဲ့ function မျိုးပါ။
Memory သက်သာဖို့ ရည်ရွယ်ပါတယ်။
စားပွဲပေါ်မှာ laptop တစ်လုံးချင်းပြသလိုမျိုး ဖြစ်ပါမယ်။

##################################################################################

1. List Comprehension
   - Creating new list
   - Transforming data
   - Filtering data

ရှိပြီးသား list တစ်ခုကို အခြေခံပြီး list အသစ်တစ်ခုကို တိုတိုတုတ်တုတ်နဲ့ အလွယ်တကူ တည်ဆောက်တဲ့ နည်းလမ်းဖြစ်ပါတယ်။
ကြာချိန်က ပုံမှန် for loop ထက် ပိုမြန်ပါတယ်။
ရင်းနှီးသွားပြီဆိုရင် For loop ထက်လည်း ဖတ်ရလွယ်ပါတယ်။

#########################################

1. list to new list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new2 = [n + 5 for n in l]
print(new2)

2. Transforming data (Kg to Lb)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [round(kg * 2.2, 2) for kg in kgs]
print(lbs)

3. Filtering data (even number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = [n for n in l if n % 2 == 0]

print(even_numbers2)

#########################################

1. list to new list

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     + 5
[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = []
for n in l:
    new.append(n + 5)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new2 = [n + 5 for n in l]
print(new2)

#########################################

2. Transforming data (Kg to Lb)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [kg * 2.2 for kg in kgs]
print(lbs)

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [round(kg * 2.2, 2) for kg in kgs]
print(lbs)

#########################################

3. Filtering data (even number)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for n in l:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = [n for n in l if n % 2 == 0]

print(even_numbers2)

##################################################################################

d = {
    "Mg Mg": "A",
    "Ma Ma": "A",
    "Hla Hla": "B"
}

ans = {name: grade for name, grade in d.items() if grade == "A"}
names = [name for name, grade in d.items() if grade == "A"]

print(ans)
print(names)

##################################################################################

2. Decorator

မူရင်း function ကို တိုက်ရိုက်မပြင်ပဲ
ကြားခံ function တစ်ခုနဲ့  လုပ်ဆောင်ချက်အသစ်တွေ ထပ်ပေါင်းထည့်တာမျိုးပါ။
တတိယမြောက် function ကို ဘယ်လိုအမည်ပေးမလဲဆိုတာမျိုး သိရပါမယ်။

2. Decorator
   - new and old (different name)
   - old to new  (same name)(@decorator)

#########################################

"မူရင်း function"

def f1():
    print("Hello")


def ff():
    print("Hi")
    

def fff():
    print("Bye")


#########################################

"မူရင်း function ကို တိုက်ရိုက်ပြင်"


def f1():
    print("-" * 49)
    print("Hello")
    print("-" * 49)


def ff():
    print("-" * 49)
    print("Hi")
    print("-" * 49)


def fff():
    print("-" * 49)
    print("Bye")
    print("-" * 49)
    
#########################################

"မူရင်း function ကို တိုက်ရိုက်မပြင်ပဲ decorate လုပ်"

1. အဟောင်းနဲ့ အသစ် နှစ်ခုလုံးလိုချင်ရင် မတူတဲ့အမည်ပေး 


def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)

    return f3


def f1():
    print("Hello")


z = f2(f1)

f1()
f1()
f1()
f1()
f1()

z()

#########################################

2. အဟောင်းနေရာမှာ အသစ်ကို အစားဝင်ချင်ရင် အမည်တူပေး


def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3


def f1():
    print("Hello")


f1 = f2(f1)

f1()
f1()
f1()
f1()
f1()

#########################################

"shortcut ဖြင့် အမည်တူပေးနည်း"

def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)
    return f3


@f2
def f1():
    print("Hello")


f1()
f1()
f1()
f1()
f1()

#########################################

"အမည်တူပေးနည်း နှစ်မျိုး"

f1 = f2(f1)

@f2
def f1():
    print("Hello")

#################################################################################

3. Generator
   - yield
   - eg.range, summation, even
   
Data တွေကို တစ်ခါတည်း အကုန်မထုတ်ပေးဘဲ လိုအပ်တဲ့အချိန်မှ တစ်ခုချင်းစီ ထုတ်ပေးတဲ့ function မျိုးပါ။
Memory သက်သာဖို့ ရည်ရွယ်ပါတယ်။
စားပွဲပေါ်မှာ laptop တစ်လုံးချင်းစီပြသလိုမျိုး ဖြစ်ပါမယ်။

#########################################

yield လေးခုဆိုရင် လေးကြိမ်ထုတ်ပေးနိုင်

def f():
    yield 1
    yield 1
    yield 1
    yield 1
        
 
အဆုံးမရှိထုတ်ချင်ရင် while loop
       
def f():
    while True:
        yield 1
        

1, 2, 3 စသဖြင့် အမျိုးမျိုးထုတ်ချင်ရင် လှည့်ပတ်ရေး

def f():
    n = 0
    while True:
        n += 1
        yield n
        
        
# 1 to 9        
def f():
    n = 0
    while True:
        n += 1
        if n >= 10:
            break
        yield n
      
 
ရပ်ဖို့အတွက် break သုံး
               
def f(start, stop, step=1):
    n = start
    while True:
        if n >= stop:
            break
        yield n
        n += step
        
ရပ်ဖို့အတွက် condition သုံး

def f(start, stop, step=1):
    ans = start
    while ans < stop:
        yield ans
        ans += step
        
        
#########################################


def f():
    yield "a"
    yield 1.5
    yield "apple"
    yield 10


x = f()

print(next(x))
print(next(x))
print(next(x))
print(next(x))

#########################################

"ဥပမာ ငါးခု"

1. range


def f(start, stop, step):
    ans = start
    while ans < stop:
        yield ans
        ans += step


number_sequence = f(2, 11, 2)
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))
print(next(number_sequence))

#########################################

2. summation

summation of 1 = 1
summation of 2 = 1 + 2 = 3                2
summation of 3 = 1 + 2 + 3 = 6            3
summation of 4 = 1 + 2 + 3 + 4 = 10       4


def summation():
    ans = 1
    n = 2
    while True:
        yield ans
        ans += n
        n += 1


s = summation()
print(next(s))
print(next(s))
print(next(s))
print(next(s))

#########################################


def summation():
    ans = 1
    n = 2

    while True:
        yield ans
        ans += n
        n += 1


s = summation()

for i in range(1, 1001):
    print(f"summation of {i} = {next(s)}")

#########################################

n = 1
for s in summation():
    print(f"Summation of {n} = {s}")
    if n == 1000:
        break
    n += 1

#########################################

3. factorial


def factorial():
    ans = 1
    n = 2
    while True:
        yield ans
        ans *= n
        n += 1


n = 1
for s in factorial():
    print(f"Factorial of {n} = {s}")
    if n == 10:
        break
    n += 1

#########################################

4. even_number


def even_number():
    ans = 2
    while True:
        yield ans
        ans += 2


def even_number():
    ans = 0
    while True:
        ans += 2
        yield ans


e = even_number()

for _ in range(100):
    print(next(e))

#########################################

5. A to Z


def A_Z():
    o = 65
    for _ in range(26):
        yield chr(o)
        o += 1


def က_အ():
    o = 4096
    for _ in range(34):
        yield chr(o)
        o += 1


def a_z():
    o = 97
    for _ in range(26):
        yield chr(o)
        o += 1

##################################################################################

4. Lambda function

အမည်ပေးစရာမလိုတဲ့ တစ်ခါသုံး function ဖြစ်ပါတယ်။

lambda x, y: x + y
lambda x, y: x - y
lambda x, y=0: x + y
lambda x, y, /: x + y
lambda : print("-" * 42)
lambda name, age, ph_no: print(name, age, ph_no)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def add(x, y=0):
    return x + y


def add(x, y, /):
    return x + y


def line():
    print("-" * 42)


def info(name, age, ph_no):
    print(name, age, ph_no)


-----------------------------------------

For garbage collection system   

x = 1
y = 2
z = x + y
print(z)
>> int(1), int(2) ->  int(3)
>> 28 bytes 28 bytes 28 bytes -> 84 bytes, int 3

print(1 + 2)
>> 28 bytes 28 bytes 28 bytes -> 0 bytes , int 0

-----------------------------------------

Test purpose

line = lambda :print("-" * 42)
line()


def line():
    print("-" * 42)


line()

##################################################################################

5. Higher-Order Functions

higher ဆိုတာက ပိုကြီးတာကို ပြောတာပါ။ first order function ထက် ပိုကြီးတာတွေပေါ့။
တနည်းအားဖြင့် second order function, third order function, . . .  တွေကို ပေါင်းပြီး ခေါ်လိုက်တဲ့ အခေါ်အဝေါ်ပေါ့။

သင်္ချာမှာ first order function ဆိုတာက f(x) ကို ပြောတာပါ။
x တန်ဖိုးထည့်ရင် y တန်ဖိုးထွက်မယ်ဆိုတာမျိုးပါ။
first order function ထုတ်ပေးရင်တော့ second order function ဖြစ်သွားပါမယ်။
second order function ထုတ်ပေးရင်တော့ third order function ဖြစ်သွားပါမယ်။

အလွယ်ပြောရရင် function ထုတ်ပေးတဲ့ function မှန်သမျှကို higher-order function လို့ ခေါ်နိုင်ပါတယ်။

f(a, b, c)

f(a)(b)(c)

-----------------------------------------

First-Order Functions -> f(x)

x = 3
y = 2x = 6


def f(x):
    y = 2 * x
    return y

-----------------------------------------

Second-Order Functions (produce First-Order Functions)


def s(a):
    def f(x):
        y = 2 * x
        return y
    return f



s(a) <- Second-Order Functions
f(x) <- First-Order Functions

-----------------------------------------

Third-Order Functions (produce Second-Order Functions)

def t():
    def s(a):
        def f(x):
            y = 2 * x
            return y

        return f

    return s

-----------------------------------------

fourth order function

def ff():
    def t():
        def s(a):
            def f(x):
                y = 2 * x
                return y

            return f
        return s
    return t

-----------------------------------------

"Sample code"


def t(a):
    def s(b):
        def f(c):
            y = a * b * c
            return y
        return f
    return s


ans = t(2)(3)(4)  # a=2, b=3, c=4

print(ans)

-----------------------------------------

first order function, normal function    -->  data

second order function                    -->  1st function
third order function                     -->  2nd function
fourth order function                    -->  3rd function

##################################################################################

6. Closure

Closing something လို့ အဓိပ္ပါယ်ရပါတယ်။

ပုံမှန်အားဖြင့် local data တွေက ဖျက်ခံရပါတယ်။ Closed လုပ်ထားရင်တော့ ဆက်ပြီးရှိနေပါတယ်။

Data တွေကို Global အနေနဲ့ မသုံးချင်တဲ့အခါ local မှာ ထားရင်လည်း ဖျက်ခံရမှာစိုးတဲ့အခါ closure ဆိုတဲ့ နည်းလမ်းကို အသုံးပြုပါတယ်။

- a process of closing somthing
- closing different data => s(2), s(3), s(7)

- data hiding (closing data)
- function factories
- decorators  (closing fun)

-----------------------------------------


def s(a):

    def f(x):
        y = a * x
        return y

    return f


dollar_kyat = s(5000)
kyat_dollar = s(1/5000)
dollar_baht = s(35)
kg_lb = s(2.2)

print(dollar_kyat(10))
print(kyat_dollar(50000))
print(dollar_baht(10))

print(dollar_kyat.__closure__)
print(kg_lb.__closure__)

-----------------------------------------

def s(a):

    def f(x):
        y = a * x
        return y

    return f


z = s(2)

-----------------------------------------

z = s(2) is same as z = f() that closed a=2


def f(x):
    y = 2 * x
    return y

z = f

-----------------------------------------

z = s(3) is same as z = f that closed a=3


def f(x):
    y = 3 * x
    return y

z = f

-----------------------------------------


def s(a):

    def f(x):
        y = a * x
        return y

    return f


multiply_2 = s(2)  # a=2
print(multiply_2(1))      # 2 * x = 2
print(multiply_2(2))      # 2 * x = 4
print(multiply_2(3))      # 2 * x = 6

multiply_3 = s(3)  # a=3
print(multiply_3(1))      # 3 * x = 3
print(multiply_3(2))      # 3 * x = 6
print(multiply_3(3))      # 3 * x = 9

multiply_79 = s(79)

-----------------------------------------


def add_factory(n):
    def add(x):
        return x + n
    return add


add_1 = add_factory(1) # closed 1
print(add_1(2))

add_7 = add_factory(7) # closed 7
print(add_7(2))

-----------------------------------------

def alcohol_permit_germany(age):
    return age >= 16

def alcohol_permit_england(age):
    return age >= 19

def alcohol_permit_japan(age):
    return age >= 21


alcohol_permit_germany(20)  =>  True
alcohol_permit_england      =>  True
alcohol_permit_japan        =>  False

-----------------------------------------

def alcohol_permit(age):
    return age >= 16

def alcohol_permit(age):
    return age >= 19

def alcohol_permit(age):
    return age >= 21

age by germany = 16
age by england = 19
age by japan = 21

def alcohol_permit(age):
    return age >= age_by_country

-----------------------------------------

Function factories


def factory(age_by_country):

    def alcohol_permit(age):
        return age >= age_by_country

    return alcohol_permit


age_by_country = 21  # 19, 16, 21, 18 by location of country
age = 16             # now - birthyear , 2026 - 2010

alcohol_permit = factory(age_by_country)  # 19, 16, 21, 18

if alcohol_permit(age):
    print("You can buy.")

else:
    print("You can not buy.")

-----------------------------------------

Decorators  (closing fun)


def f2(x):
    def f3():
        print("-" * 41)
        x()
        print("-" * 41)

    return f3


def f1():
    print("Hello")


z = f2(f1)

print(z.__closure__)

-----------------------------------------


def s(a, b, c):

    def f1(x):
        y = a + x
        return y

    def f2(x):
        y = a + b + x
        return y

    def f3(x):
        y = a + b + c + x
        return y

    return f1, f2, f3


x, y, z = s(1, 2, 3)

print(s.__closure__)     # None
print(x.__closure__)     # closed  1
print(y.__closure__)     # closed  1 and 2
print(z.__closure__)     # closed  1 and 2 and 3

##################################################################################

"""

