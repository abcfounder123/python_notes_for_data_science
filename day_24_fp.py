
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


"""

