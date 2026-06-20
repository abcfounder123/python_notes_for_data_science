
"""

"CustomTypes"

Exercises

Step.1
Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

Step.2
ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။

Step.3
သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။

Step.4
Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။

Step.5
Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

Step.6
dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

Step.7
သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။

Step.8
သင်္ကေတနဲ့ object ဖန်တီးချင်တာပါ။ literal(), fun

Step.9
သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။

Step.10
dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။

Step.11
Memory သက်သာအောင် တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီးပြီး ဝေမျှသုံးစေချင်တာပါ။ new(), cache

3 min

#################################################

Step.1 (Draw Dollar Type)

Dollar ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။

class    -  Dollar
data     -  n
methods  -  add()

#################################################

Step.2 (Representation string -> "1 dollar")

ကိုယ်စားပြုမယ့်စာတန်ဖိုးကို 1 dollar လို့ ပေးချင်တာပါ။

def __repr__(self):
    return f"{self.n} dollar"

#################################################

Step.3 ( + ) (__add__)

သင်္ကေတနဲ့ ပေါင်းချင်တာပါ။

def __add__(self, other):
    return self.n + other.n

#################################################

Step.4 (result of addition => 3 dollar )

Dollar နှစ်ခုပေါင်းတဲ့အခါ ရလဒ်ကို dollar အဖြစ်နဲ့ပဲ လိုချင်တာပါ။

>> Dollar(self.n + other.n)

#################################################

Step.5 ( Design for Kyat )

Kyat ဆိုတဲ့ class ဒီဇိုင်းဆွဲတာပါ။


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kyat(self.n + other.n)

    def __repr__(self):
        return f"{self.n} kyat"


#################################################

Step.6 (dollar + kyats)

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် ပေါင်းချင်တာပါ။

1 dollar + 10000 kyats => 3 dollar
10000 kyats + 1 dollar => 15000 kyats

#################################################

if type(other) == Dollar:
    return Dollar(self.n + other.n)
if type(y) == Kyat:
    return Dollar(self.n + other.n / 5000)

#################################################

Step.7 ( - ) ( __sub__ )

သင်္ကေတနဲ့ နှုတ်ချင်တာပါ။

def __sub__(self, other):
    if type(other) is Dollar:
        return Dollar(self.n - other.n)
    elif type(other) is Kyat:
        return Dollar(self.n - other.n / 5000)

#################################################

Step.8 (literal)

သင်္ကေတနဲ့ object ဖန်တီးချင်တာပါ။

Install external pakage
1. custom-literals
2. forbiddenfruit

from custom_literals import literal

@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)

#################################################

Step.9 ( == ) ( __eq__ )

သင်္ကေတနဲ့ တန်ဖိုးတူလား နှိုင်းယှဉ်ချင်တာပါ။

def __eq__(self, other):
    return self.n == other.n

#################################################

Step.10 ( dollar == kyat )

dollar နဲ့ kyats လိုမျိုး အမျိုးအစား မတူတာတွေကို မှန်မှန်ကန်ကန် နှိုင်းယှဉ်ချင်တာပါ။

def __eq__(self, other):
    if type(other) is Dollar:
        return self.n == other.n
    if type(other) is Kyat:
        return self.n == other.n / 5000
            
#################################################

Step.11

Memory သက်သာအောင် တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီးပြီး ဝေမျှသုံးစေချင်တာပါ။

တန်ဖိုးတူခဲ့ရင် တစ်ကြိမ်ပဲ ဖန်တီး  =>  new()


class Dollar:
    x = {}

    def __new__(cls, n):
        if n in Dollar.x.keys():
            return Dollar.x[n]                # 0x100d52120
        else:
            new = super().__new__(cls)        # 0x100d52120
            new.n = n                         # 0x100d52120 <- 
            Dollar.x[n] = new
            return new


##################################################################################################

"""
