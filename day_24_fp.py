
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

7.  Map

ကီလိုဂရမ်ကနေ ပေါင်အဖြစ် ပြောင်းတာမျိုး ၊ ဒေါ်လာကို ကျပ်ပြောင်းတာမျိုး data တွေကို transform လုပ်ဖို့အတွက် သုံးပါတယ်။

- create a connection between fun and data, data pip line
- transform(kg to lb) (1 litre, 1kg, 2.2lb)

#########################################

>> transform(kg to lb)


def f1(kg):
    print(f"f1({kg})")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#########################################

lbs = []

for kg in kgs:                   # for loop
    lbs.append(f1(kg))

lbs2 = [f1(kg) for kg in kgs]    # list comprehension

lbs3 = map(f1, kgs)              # map => a connection between f1 and kgs


#########################################

List comprehension example


def f1(kg):
    print("h")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [f1(kg) for kg in kgs] # 10 s

print(l)

#########################################

f1
f1
f1
f1
f1
f1
f1
f1
f1
f1
[2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8, 22.0]

500 MB => 5 minutes

1 MB => 1 sec

1 MB => 1 sec

1 MB => 1 sce

#########################################

Map example


def f1(kg):
    print("h")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = map(f1, kgs)

print(next(l))  # 1s

#########################################

f1
2.2

##################################################################################

Time consumption

all data => 1 hour

1 page  => 1 sec

##################################################################################

Memory consumption

lbs = [2.2, 4.4, 6.6, 8.8, 11.0, 13.2, 15.4, 17.6, 19.8, 22.0]
list = 50 bytes
float 10 = 300 bytes
total = 350 bytes

map = 50 bytes
next(l)
float 1 = 30 bytes = 0 bytes
next(l)
float 1 = 30 bytes = 0 bytes

##################################################################################

kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lbs = [f1(kg) for kg in kgs]

list      => 50
int 10    => 280       
lbs       => 50
float 10  => 300 bytes 
total     => 680 bytes

########################################


def f1(kg):
    print(f"f({kg})")
    return round(kg * 2.2, 2)


kgs = range(1, 11, 1)
l = map(f1, kgs)

print(next(l))

########################################

range(1, 11) => 30
map     => 30 byte
int 1   => 28 byte  => 0 bytes
float 1 => 30 bytes => 0 bytes

total   => 60 to 118

##################################################################################

Pip line

1000 GB  (1 page = 1MB )

8 GB

database = 1 page (next value)  900  100
pip_line = map(negative_word, database)

total = 0  -> 10 -> 18 -> 100_000

##################################################################################

In List Comprehension or 'for loop',
if 1 error, None of result.


def f1(kg):
    print(f"f1({kg})")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]   # 11 => 10 + 1(error)
lbs = [f1(kg) for kg in kgs]
print(lbs)

#########################################

Map can work well until error.


def f1(kg):
    print(f"f1({kg})")
    return round(kg * 2.2, 2)


kgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]   # 11 => 10 + 1(error)
lbs = map(f1, kgs)
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))
print(next(lbs))  # error

##################################################################################

8. Filter
- Filtering data

လိုအပ်တဲ့ data ကို စစ်ထုတ်ဖို့အတွက် သုံးပါတယ်။
စုံကိန်းတွေကိုပဲ စစ်ထုတ်တာမျိုး ၊ အောင်စာရင်းထဲက ဂုဏ်ထူးထွက်တဲ့ ကျောင်းသားတွေကိုပဲ စစ်ထုတ်တာမျိုးပေါ့။

-----------------------------------------

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

#########################################

Filtering data (even number)

1. for loop example

def is_even(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for n in l:
    if is_even(n):
        even_numbers.append(n)

print(even_numbers)

#########################################

2. LC example

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
leven_numbers = [n for n in l if is_even(n)]   # [2, 4, 6, 8, 10]

print(leven_numbers)

#########################################

2. filter example

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, l)

print(next(f))
print(next(f))

#########################################


def is_even(n):
    print(f"is even({n})")
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, l)

print(next(f))  #  1 from list , is_even(1) => 2 from list , is_even(2) => 2
print(next(f))  #  3 from list , is_even(3) => 4 from list , is_even(4) => 4

#########################################

Time and memory

After 10s,  [2, 4, 6, 8, 10]


2            after 2s
4            after 2s
6            after 2s
8            after 2s
10           after 2s

##################################################################################

9. Reduce
data တွေကို တစ်ခုတည်းအဖြစ် လျော့ချဖို့သုံးပါတယ်။
ဘာသာရပ်ခြောက်ခုရဲ့ အမှတ်စာရင်းခြောက်ခုကို စုစုပါင်းရမှတ်ဆိုပြီး တစ်ခုတည်းအဖြစ် လျော့ချလိုက်တာမျိုးပါ။

-----------------------------------------

- reducing data
- all data to 1 data

#########################################

numbers to total
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] to 55

#########################################


from functools import reduce


def add(a, b):
    print(f"add({a}, {b})")
    return a + b


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = reduce(add, l)  # add(1, 2) = 3 -> add(3, 3) = 6 -> add(6, 4) = 10 ... => 55

print(r)

##################################################################################

10. Data (Transform, filter, reduce)

1. map      =>   kg to lb                 =>   10 to 10

2. filter   =>   even numbers from list   =>   10 to 5

3. reduce   =>   all marks to total marks =>   6 to 1

-----------------------------------------

"Data ပြောင်းလဲနည်း သုံးမျိုး"

Data တွေကို Transform, filter, reduce ဆိုပြီး ပုံစံသုံးမျိုးနဲ့ ပြောင်းလဲနိုင်ပါတယ်။

Transform လုပ်ချင်တဲ့အခါ map ကို သုံးနိုင်ပါတယ်။
1. map => kg to lb  => 10 to 10

လိုချင်တာကို စစ်ထုတ်ချင်တဲ့အခါ filter ကို သုံးနိုင်ပါတယ်။
2. filter => even numbers from list => 10 to 5

တစ်ခုတည်းအဖြစ် လျော့ချချင်တဲ့အခါ reduce ကို သုံးနိုင်ပါတယ်။
3. reduce => all data -> 1 data (total marks)

##################################################################################

11. Recursion

1. Direct Recursion ( tail, head, tree, nested )
2. Indirect Recursion

- recursive program

Recursion example => fibonacci

Recursion and cache
1. Normal recursion
2. Recursion with cache
3. Recursion with lru cache  (Least Recently Used Cache)

-----------------------------------------

recursion က နည်းနည်းရှုတ်ပေမယ့် မှတ်စရာ ဒီနှစ်ခုပဲရှိပါတယ်။

1. Fibonacci လိုမျိုး တစ်ဆင့်ချင်းဖြေရှင်းရမယ့် နေရာမှာသုံး
2. လိုအပ်ပါက မှတ်တမ်းယူထားရန် (cache သုံးရန်)

#########################################

p1
p2
p3
pr    tail

-----------------------------------------

pr    head
p1
p2
p3

-----------------------------------------

pr       tree
pr
                              pr

                        pr          pr

                    pr      pr    pr     pr

-----------------------------------------

pr(pr)   nested

#########################################

a. Tail Recursion


def f(n):
    if n > 0:
        print(n)
        f(n - 1)  # tail
    return


f(3)


    if 3 > 0:
        print(3)
        if 2 > 0:
           print(2)
           if 1 > 0:
              print(1)
              if 0 > 0:
                  print(n)
                  f(n - 1)
              return            stop f(0)
           return               stop f(1)
        return                  stop f(2)
    return                      stop f(3)

#########################################

b. Head Recursion

def f(n):
    if n > 0:
        f(n - 1)  # head
        print(n)
    return None


f(3)

#########################################


    if 3 > 0:
        if 2 > 0:
            if 1 > 0:
                if 0 > 0:
                    f(n - 1)
                    print(n)
                return         stop f(0)
                print(1)
            return             stop f(1)
            print(2)
        return                 stop f(2)
        print(3)
    return                     stop f(3)


#########################################

Tail and Head


def t(n):
    if n > 0:
        print(n)
        t(n - 1) # tail


def h(n):
    if n > 0:
        h(n - 1)  # head
        print(n)


t(5)  #  5 4 3 2 1
h(5)  #  1 2 3 4 5

#########################################

c. Tree Recursion

2 or more recursive program

f()      => recursive program
f()      => recursive program

#########################################


def f(n):
    if n > 0:
        print(n)
        f(n - 1)   # calling once
        f(n - 1)   # calling twice
    return

f(5)

-----------------------------------------


if 3 > 0:
    print(3)
    if 2 > 0:
        print(2)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
        return                  f(1)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
        return                  f(1)
    return                      f(2)

    if 2 > 0:
        print(2)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
        return                  f(1)
        if 1 > 0:
            print(1)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
            if 0 > 0:
                print(n)
                f(n - 1)
                f(n - 1)
            return              f(0)
        return                  f(1)
    return                      f(2)

return                          f(3)

-----------------------------------------

3

2
1
1

2
1
1



-----------------------------------------

                           f(3)                                            1

                 f(2)                   f(2)                               2

            f(1)     f(1)          f(1)        f(1)                        4

        f(0) f(0)  f(0) f(0)    f(0) f(0)     f(0) f(0)                    8
        

recursion depth = 4

----------------------------------------------------------------------------------

                                                f(4)

                           f(3)                                              f(3)

                 f(2)                   f(2)                     f(2)                   f(2)

            f(1)     f(1)          f(1)        f(1)         f(1)     f(1)          f(1)        f(1)

        f(0) f(0)  f(0) f(0)    f(0) f(0)     f(0) f(0)  f(0) f(0)  f(0) f(0)    f(0) f(0)     f(0) f(0)      

----------------------------------------------------------------------------------

4
3
2
1
1
2
1
1
3
2
1
1
2
1
1

----------------------------------------------------------------------------------

f(5)

5

4
3
2
1
1
2
1
1
3
2
1
1
2
1
1

4
3
2
1
1
2
1
1
3
2
1
1
2
1
1

----------------------------------------------------------------------------------


def f(n):
    if n > 0:
        print(n)
        f(n - 1)
        f(n - 1)
        f(n - 1)
    return


f(3)

-----------------------------------------

                                3                            1

                 2              2              2             3

            1   1   1       1   1   1      1   1   1         9

           000 000 000     000 000 000    000 000 000        27

##################################################################################

d. Nested Recursion

f()      => normal recursive program
f(f())   => nested recursive program

#########################################


def f(n):
    print(f"f({n})")
    if n > 100:
        return n - 10
    else:
        return f(f(n+11))


ans = f(99)
print(ans)

-----------------------------------------

1. f(99)        =>  return f(f(110))  =>  ?
2. f(f(110))
3. f(100)
4. f(f(111))
5. f(101)
>> 91

-----------------------------------------

                            f(99)
                            f(110)
                            f(100)
                            f(111)
                            f(101)

f(99)  =>  recursive count  = 5
f(98)  =>  recursive count  = 7
f(97)  =>  recursive count  = 9
f(96)  =>  recursive count  = 11
f(49)  =>  recursive count  = ?

##################################################################################

2. Indirect Recursion

Indirect recursion between A() and B().

A() calls B() and B() calls A().

A(5) => 5
B(4) => 4
A(3) => 3
B(2) => 2
A(1) => 1
B(0) =>

#########################################


def A(n):
    print(f"A({n})", end=" => ")
    if n > 0:
        print(n)
        B(n-1)


def B(n):
    print(f"B({n})", end=" => ")
    if n > 0:
        print(n)
        A(n-1)


A(5)

##################################################################################

Recursion example => fibonacci

f0 = 0
f1 = 1

f2 = 1
f3 = 2
f4 = 3
f5 = 5
f6 = f5 + f4
f10 = f9 + f8
f100 = f99 + f98
fn = f(n-1) + f(n-2)

-----------------------------------------

0 1 1 2 3 5 8 13 21 34  .....      Ans
0 1 2 3 4 5 6  7  8  9            Fibonacci numbers

f0 = 0
f1 = 1

fn = f(n-1) + f(n-2)

#########################################


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#########################################

"Test"


def fib(n):
    print(f"f({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


ans = fib(3)
print(ans)

-----------------------------------------

                                     fib(3)

                              fib(2)    +   fib(1)

                          f(1) + f(0)

5
-----------------------------------------

                                         4

                                    3         2

                                2      1    1    0

                             1    0

9
-----------------------------------------

Normal recursion

                                                     fib(5)

                                    fib(4)                                       fib(3)

                         fib(3)                 fib(2)                    fib(2)        fib(1)

                 fib(2)        fib(1)       fib(1)    fib(0)          fib(1)    fib(0)

             fib(1)    fib(0)

15
-----------------------------------------

Recursion with cache

                                                           fib(5)

                                    fib(4)                                       fib(3)

                         fib(3)                 fib(2)

                 fib(2)        fib(1)

             fib(1)    fib(0)

9
----------------------------------------------------------------------------------

1. Normal recursion


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


-----------------------------------------

"Test"

a = 0

def fib(n):
    global a
    a += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


ans = fib(25)
print(ans)
print(a)

#########################################

2. Recursion with cache


x = {
    0: 0,
    1: 1,
}


def fib(n):
    if n in x:
        return x[n]
    else:
        ans = fib(n-1) + fib(n-2)
        x[n] = ans
        return ans


-----------------------------------------

a = 0

x = {
    0: 0,
    1: 1,
}


def fib(n):
    global a
    a += 1
    if n in x:
        return x[n]
    else:
        ans = fib(n-1) + fib(n-2)
        x[n] = ans
        return ans


ans = fib(25)
print(ans)
print(a)

##########################################

fib(25)
1. Normal recursion = 242785
2. Recursion with cache = 49

#########################################

3. Recursion with lru cache


from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        

-----------------------------------------

"Test"

from functools import lru_cache

a = 0

@lru_cache
def fib(n):
    global a
    a += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


ans = fib(25)
print(ans)
print(a)

#########################################

fib(25)
1. Normal recursion         => 242785
2. Recursion with cache     => 49
3. Recursion with lru cache => 26

#########################################

fib(40)
1. Normal recursion         =>  f40 = 20 sec and 331_160_281
2. Recursion with lru cache =>  f40 =  0 sec and 41

lru = least recently used

##################################################################################

Extra

Add new
d["age"] = 20

Access
d["age"]

Update
d["age"] += 1
d["age"] = 21

##################################################################################

12. Partial

power function    =>   base, exponent  => 2 ** 2, 3 ** 2, 4 ** 2, 5 ** 2 | 2 ** 3, 3 ** 3, 4 ** 3, 5 ** 3
square function   =>   base ** 2
cube   function   =>   base ** 3

#########################################

fun => argument 1, argument 2, argument 3, argument 4, argument 5, argument 6

#########################################

power(base, exponent)
square(5) => power(base=5, exponent=2)  => 5 ** 2  => 25
cube(5) => power(base=5, exponent=3)    => 5 ** 3  => 125

#########################################

from functools import partial


def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)  # power(base, exponent=2)
cube = partial(power, exponent=3)  # power(base, exponent=3)

print(power(5, 3))
print(square(5))
print(cube(5))

##################################################################################

13. Currying

- Haskell Curry
- f(x, y) => f(x)(y)
- multiply(x, y, z) => multiply(x)(y)(z)
- nested function

1. Reusability
2. Function composition
3. Delayed Execution

##################################################################################

Currying methods example.1
- multiply(x, y, z) => multiply(x)(y)(z)

def multiply(x, y, z):
    return x * y * z


def multiply(x):
    def f2(y):
        def f3(z):
            return x * y * z
        return f3
    return f2

#########################################

def multiply(x):
    def f2(y):
        def f3(z):
            return x * y * z
        return f3
    return f2


b = multiply(1) # x=1 => f2
print(b)

c = b(2) # x=1, y=2 => f3
print(c)

ans = c(3) # x=1, y=2, z=3 => x * y * z => 6
print(ans)

ans = multiply(1)(2)(3)
print(ans)

#########################################

Currying methods example.2
- tax_calculator(tax_rate, price)  =>  tax_calculator(tax_rate)(price)

tax_rate = 5%, 10%, 15%
price = ?

food_tax = 5%
electronic_tax = 10%
house_tax = 15%
price = ?

#########################################

1. Reusability
   - tax_calculator() => food_tax_calculator(), electronic_tax_calculator()


def tax_calculator(tax_rate):
    def f2(price):
        return price + (price * tax_rate)
    return f2


food_tax_calculator = tax_calculator(0.05)
electronic_tax_calculator = tax_calculator(0.1)
house_tax_calculator = tax_calculator(0.15)

print(tax_calculator(0.05)(100))
print(food_tax_calculator(100))
print(electronic_tax_calculator(1200))
print(house_tax_calculator(1_000_000))

#########################################

3. Delayed Execution

student =>  roll, name, result(pass, fail)


def student(roll, name):
    print("roll = ", roll)
    print("name = ", name)
    def f2(result):
        print(f"roll {roll} (exam = {result})")
    return f2


s1 = student(1, "Mg Mg")  # Execution with first data
# s1("pass") # Execution with second data

##################################################################################

14. Lazy Evaluation

- memory efficiency
- performance
- infinite series

generator = 50 bytes
next value = 28 bytes  (int)
total = 50 + 28

#########################################


def f():
    for n in range(1, 1_000_001):
        yield n


numbers1 = f()
print(next(numbers1))   # 1 sec

numbers = (n for n in range(1, 1_000_001))
print(numbers)
print(next(numbers))    # 1 sec

#########################################

15. Eager Evaluation

- creating all data in RAM
- ready to use all data

list = 50 bytes
int = 28 bytes
total = 50 + 28 million

#########################################

numbers = [n for n in range(1, 1_000_001)]  # 1_000_000 (int objects)

print(numbers[0]) # 1_000_000 sec
print(numbers)

##################################################################################

16. list comprehension to generator comprehension
    => [] to ()
    => (n for n in range(1, 1_000_001)) will create following generator object

#########################################


def generator_object():
    for n in range(1, 1_000_001):
        yield n
        

numbers = generator_object()
print(numbers)
print(next(numbers))

numbers = (n for n in range(1, 1_000_001))  # same as above generator, generator comprehension
print(numbers)
print(next(numbers))

##################################################################################

17. Lazy Evaluation Vs Eager Evaluation

RAM 8 GB -> can not create one billion objects by Eager Evaluation   + SSD 20 GB

numbers = [n for n in range(1, 1_000_000_001)]    # 28 GB

for n in numbers:
    print(n)

#########################################

Generator can create a series of one billion objects by Lazy Evaluation.

numbers = (n for n in range(1, 1_000_000_001))     # 50 + 28 bytes

for n in numbers:
    print(n)

##################################################################################################


"""

