
"""

Exercises (25)

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

------------------------------------------

4. is_lower (a to z တွေက lower case characterဖြစ်ပါတယ်။)

------------------------------------------

5. is_upper (A to Z တွေက upper case characterဖြစ်ပါတယ်။)

------------------------------------------

6. is_alphabet (a to z တွေက english အက္ခရာဖြစ်ပါတယ်။)

------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )

------------------------------------------

9. less number ( n1 < n2 )

------------------------------------------

10. leap year (ရက်ထပ်နှစ်) (Julian calendar)
 >> divisible by 4  (y % 4 == 0)

------------------------------------------

11. leap year (ရက်ထပ်နှစ်) (Gregorian calendar)
>> divisible by 400 ( eg. 2000, 1600 )       ( y % 400 == 0 )
>> divisible by 4 and not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
>> Rule.1 or Rule.2

------------------------------------------

12. leap year (ရက်ထပ်နှစ်) Modern calendar
>> divisible by 400 and not divisible by 3200  ( y % 400 == 0 and y % 3200 != 0 )
>> divisible by 4 and not divisible by 100     ( y % 4 == 0 and y % 100 != 0 )

------------------------------------------

Summary
=> +1 days by 4 years                     <---  Julian
=> -3 days by 400 years                   <---  Gregorian
=> -1 days by 3200 years                  <---  Modern

------------------------------------------

13. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15

------------------------------------------

14. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

------------------------------------------

15. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )
    - "I go to school."
    - ".loohcs ot og I"

------------------------------------------

16. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

------------------------------------------

17. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

Add item to dict
d["I"] = 1

Access dict value
d["I"]

Update dict value
d["I"] = 2
d["I"] += 1

------------------------------------------

18. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)

------------------------------------------

19. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

20. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

21. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။

------------------------------------------

22. Lower case to upper case

------------------------------------------

23. Upper case to lower case 

------------------------------------------

24. upper()

------------------------------------------

25. lower()

------------------------------------------

26. Linear search

------------------------------------------

27. Binary search

------------------------------------------------------------------------------------

Answers

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

4. is_lower (a to z တွေက lower case characterဖြစ်ပါတယ်။)


def is_lower(c):
    return c in "abcdefghijklmnopqrstuvwxyz"
    

------------------------------------------

5. is_upper (A to Z တွေက upper case characterဖြစ်ပါတယ်။)


def is_upper(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


------------------------------------------

6. is_alphabet (a to z တွေက english အက္ခရာဖြစ်ပါတယ်။)


def is_alphabet(c):
    return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def palindrome(s):
    return s == s[::-1]


------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

------------------------------------------

9. less number ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2

------------------------------------------

"Three steps of greater number"

greater_number(2, 1)   =>  2      <-- n1           1sec    1    1
greater_number(1, 2)   =>  2      <-- n2           2       2    1
greater_number(2, 2)   =>  2      <-- n1 or n2     3       2    1


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

------------------------------------------

10. leap year (ရက်ထပ်နှစ်) (Julian calendar)

1. divisible by 4  (y % 4 == 0)


def is_leap_year(y):
    return y % 4 == 0


------------------------------------------

11. leap year (ရက်ထပ်နှစ်) (Gregorian calendar)

1. divisible by 400 ( eg. 2000, 1600 )       ( y % 400 == 0 )
2. divisible by 4 and not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
Rule.1 or Rule.2


def is_leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)


------------------------------------------

12. leap year (ရက်ထပ်နှစ်) Modern calendar

1. divisible by 400 and not divisible by 3200  ( y % 400 == 0 and y % 3200 != 0 )
2. divisible by 4 and not divisible by 100     ( y % 4 == 0 and y % 100 != 0 )
  

def is_leap_year(y):
    return ( y % 400 == 0 and y % 3200 != 0 ) or ( y % 4 == 0 and y % 100 != 0)


------------------------------------------

Summary
=> +1 days by 4 years                     <---  Julian
=> -3 days by 400 years                   <---  Gregorian
=> -1 days by 3200 years                  <---  Modern

------------------------------------------

13. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15


def summation(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i
    return ans


------------------------------------------

14. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120


def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


------------------------------------------

15. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )
    - "I go to school."
    - ".loohcs ot og I"


def reverse_string(s):
    return s[::-1]


------------------------------------------

16. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)


def count_vowels(s):
    t = 0
    for c in s:
        if c in "aeiouAEIOU":
            t += 1
    return t


------------------------------------------

17. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

Add item to dict
d["I"] = 1

Access dict value
d["I"]

Update dict value
d["I"] = 2
d["I"] += 1

if c not in d:
if c not in d.keys():

------------------------------------------


def count_vowels(s):
    d = {}
    for c in s:
        if c in "aeiouAEIOU":  
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
    return d


------------------------------------------

18. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)


def sum_of_list(lst):
    t = 0
    for n in lst:
        t += n
    return t


------------------------------------------

19. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)


def max(l):
    m = l[0]

    for n in l[1:]:
        m = greater_number(m, n)

    return m
    

------------------------------------------

20. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)


def min(l):
    m = l[0]

    for n in l[1:]:
        m = less_number(m, n)

    return m


------------------------------------------

21. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။


def find_max_min(l):
    return (max(l), min(l))


------------------------------------------

Wrong Sample


def find_max_min2(l):
    m = l[0]

    for n in l[1:]:
        if m > n:
            pass
        else:
            m = n

    min = l[0]

    for n in l[1:]:
        if min < n:
            pass
        else:
            min = n

    return (m, min)
    
    
------------------------------------------    

Test


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


def max(l):
    m = l[0]

    for n in l[1:]:
        m = greater_number(m, n)

    return m


def min(l):
    m = l[0]

    for n in l[1:]:
        m = less_number(m, n)

    return m


def find_max_min(l):
    return (max(l), min(l))


numbers = [100, 300, 200, 1000, 400, 350, 50]
ans = find_max_min2(numbers)
print(ans)

------------------------------------------
    
22. Lower case to upper case

"a" to "A"

1. ordinal number    =>  ord("a")  =>  97
2. - 32              =>  65
3. ord to chr        =>  chr(65)   =>  A


def lower_upper(l):
    return chr(ord(l) - 32)
    

------------------------------------------

23. Upper case to lower case 

"A" to "a" 

1. ordinal number    =>  ord("A")  =>  65
2. + 32              =>  97
3. ord to chr        =>  chr(97)   =>  a


def upper_lower(l):
    return chr(ord(l) + 32)


------------------------------------------

24. upper()


def upper(s):
    ans = ""

    for c in s:
        if is_lower(c):
            ans += lower_upper(c)
        else:
            ans += c

    return ans


------------------------------------------

25. lower()


def lower(s):
    ans = ""

    for c in s:
        if is_upper(c):
            ans += upper_lower(c)
        else:
            ans += c

    return ans


------------------------------------------

Test for upper


def is_lower(c):
    return c in "abcdefghijklmnopqrstuvwxyz"


def lower_upper(l):
    return chr(ord(l) - 32)


def upper(s):
    ans = ""

    for c in s:
        if is_lower(c):
            ans += lower_upper(c)
        else:
            ans += c

    return ans


s = "I go to school."

u = upper(s)
print(u)

------------------------------------------

Test for lower


def is_upper(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def upper_lower(l):
    return chr(ord(l) + 32)


def lower(s):
    ans = ""

    for c in s:
        if is_upper(c):
            ans += upper_lower(c)
        else:
            ans += c

    return ans


s = "I go to school."
u = lower(s)
print(u)

------------------------------------------

26. Linear search


def linear_search(l, element):
    for e in l:
        if e == element:
            return True
    return False


------------------------------------------

27. Binary search


[31, 42, 68, 80, 100, 150, 200]

element = 300

1. m = 80 
2. g => R = [100, 150, 200] 

1. m = 150
2. g => R = [200] 

1. m = 200
2. g => R => []

------------------------------------------ 

Greater =>  right  => [m+1:]  => [100, 150, 200]
Less    =>  left   => [:m]    => [31, 42, 68]

found = stop True 
empty = stop False

------------------------------------------


def binary_search(l, element):
    while len(l) > 0:
        t = len(l)
        m = t // 2
        middle_value = l[m]

        if element == middle_value:
            return True

        elif element > middle_value:
            l = l[m+1:]

        elif element < middle_value:
            l = l[:m]
    return False
  
  
------------------------------------------ 

Linear search Vs Binary search 

1 million elements
# binary =>  1 sec to 20 sec
# linear =>  1 sec to 1 million sec

100 elements
# binary =>  1 sec to 6 sec
# linear =>  1 sec to 100 sec

------------------------------------------------------------------------------------ 

"""
