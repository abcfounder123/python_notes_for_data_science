
"""

Function

1. Function define      =>   def
2. Function name        =>   add
3. Parameter list       =>   ()
4. Parameters           =>   n1, n2
5. Code block           =>   :
6. Documentation string =>   triple quotes (help, doc)
7. Function body        =>   programs , ans = n1 + n2
8. return statement     =>   stop, return value

help()
1. Function name
2. Parameter list
3. documentation string  (__doc__)

9. Types of function
10. Pure function
11. Exercises

################################################


def add(n1, n2):
    '''documentation string'''
    ans = n1 + n2
    return ans


################################################

Types of function
1. effect only function    =>  difference_update()
2. result only function    =>  difference()
3. effect and result       =>  pop()

################################################

pop()
effect = Remove item at index
result = removed item

Remove and return item at index (default last).

------------------------------------------

difference()
effect = -
result = a new set

Return the difference of two or more sets as a new set.
(i.e. all elements that are in this set but not the others.)

------------------------------------------

difference_update()
effect = Remove all elements of another set from this set.
result = -

Remove all elements of another set from this set.

------------------------------------------

len()
effect =
result = the number of items in a container

Return the number of items in a container.

################################################

Pure function (result only function)


Three steps of function


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

------------------------------------------


No         Date             Temperature(C)     
1     1.1.2024(6:00)               27          
2     1.1.2024(12:00)              30          
3     1.1.2024(22:00)              29          


No         Date             Temperature(C)     Fahrenheit
1     1.1.2024(6:00)               27          80.6
2     1.1.2024(12:00)              30          86.0
3     1.1.2024(22:00)              29          84.2

------------------------------------------

1. Table    <---   read_excel("excel file name")
2. column   <---   t["column name"]
3. list     <---   list()
4. new file <---   to_excel

------------------------------------------

import pandas


def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


t = pandas.read_excel("tt_2024.xlsx")
c = list(t["Temperature(C)"])         # [27, 30, 29]
f = []

for celsius in c:
    f.append(celsius_fahrenheit(celsius))

t["Fahrenheit"] = f
t.to_excel("group6_7.xlsx")

################################################################################################

Exercises


1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    return n % 2 == 0


------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    return n % 2 == 1


------------------------------------------

def is_even(n):
    return n % 2 == 0


numbers = [100, 105, 3, 9, 1000, 4, 8, 6]
even = []

for number in numbers:
    if is_even(number):
        even.append(number)

print(even)

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

"a"
"6"


def is_number(c):
    return c in "0123456789"


------------------------------------------


def is_number(c):
    return c in "0123456789"


x = '''whgfjew dhu 38dhgjhwgd 383djcgw c8'''
n = 0

for c in x:
    if is_number(c):
        print(f"We found {c}")
        n += 1

print(n)

------------------------------------------

is_alphabet (a to z တွေနဲ့ ကကြီး ခကွေးလိုမျိုးတွေက အက္ခရာဖြစ်ပါတယ်။)

4. English alphabet


def is_alphabet(c):
    return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

------------------------------------------

5. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def palindrome(s):
    return s == s[::-1]


------------------------------------------




"""
