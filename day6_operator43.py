
"""

Day.5 + Day.6

Day.5

Operator.43

1. Operation, Operator, Oparand

      1 + 2     <=    Additional Operation 
        +       <=    Additional Operator 
        1       <=    Left Operand
        2       <=    Right Operand

#################################################

2. Types of oprators 
   - unary operator    (right)
   - binary operator   (left, right)
   - ternary operator  (middle)
 
#################################################

3. Positive, Negative, Addition, Substraction

+1          <-  pos
-1          <-  neg 
1 + 2       <-  add
1 - 2       <-  sub

1 * 2       <-  mul
1 / 2       <-  truediv
1 // 2      <-  floordiv
1 % 2       <-  mod

#################################################

4. Precedence (15)

add
1 + 2 * 3
3 * 3
9

mul
1 + 2 * 3
1 + 6
7

#################################################

5. Associativity (2)
   - left-sided bind
   - right-sided bind

left-sided bind
2 ** 2 ** 3
4 ** 3
64

right-sided bind
2 ** 2 ** 3
2 ** 8
256

#################################################

Exercise

1 + 2 + 3 // 4 - 5 % 6 + 1 ** 7

1. **
>> 1 + 2 * 3 // 4 - 5 % 6 + 1

2. *
>> 1 + 6 // 4 - 5 % 6 + 1

3. //
>> 1 + 1 - 5 % 6 + 1

4. %
>> 1 + 1 - 5 + 1

5. +
>> 2 - 5 + 1

6. -
>> -3 + 1

7. +
>> -2


1. **         
2. 
3. * // %     
4. +, -, +

#################################################

Arithmetic operators (9) (e u */ +-)

1. Exponent         **
2. Unary minus      -
3. Unary plus       +
4. Multiplication   *
5. True division    /
6. Floor division   //
7. Modulus          %
8. Addition         +
9. Substraction     -

#################################################

Bitwise operators(6) (shift and or 2)
1. Left shift       <<
2. Right shift      >>
3. Bitwise AND      &
4. Bitwise OR       |
5. Exclusive OR     ^
6. Bitwise NOT      ~

#################################################

1. Left shift  ( << )

1111 << 1      --->   1110
1111 << 2      --->   1100

00000000
    1111
   1111
    1110

#################################################

2. Right shift  ( << )

1111 >> 1      --->   0111
1111 >> 2      --->   0011

    0000
    1111
     1111
    0111

#################################################

I want apple and banana.
I want apple or banana.
I want apple xor banana.

#################################################

3. Bitwise AND (&) (2 wires)


1  -----
          AND  ----  1  
1  -----

0  -----
          AND  ----  0 
1  -----

1  -----
          AND  ----  0  
0  -----

0  -----
          AND  ----  0
0  -----

0101  -----
             AND  ----  0001
0011  -----

0101 & 0011    
=> 0001

#################################################

4. Bitwise OR (|) (1 wires)


1  -----
          OR  ----  1  
1  -----

0  -----
          OR  ----  1 
1  -----

1  -----
          OR  ----  1  
0  -----

0  -----
          OR  ----  0
0  -----

0101  -----
             OR  ----   0111
0011  -----

0101 | 0011    
=> 0111

#################################################

5. Exclusive OR (^) (only one wires)


1  -----
          XOR  ----  0 
1  -----

0  -----
          XOR  ----  1 
1  -----

1  -----
          XOR  ----  1  
0  -----

0  -----
          XOR  ----  0
0  -----

0101  -----
             XOR  ----   0110
0011  -----

0101 ^ 0011    
=> 0110

#################################################

6. Bitwise NOT (~)

1  ----   NOT  ----  0

0  ----   NOT  ----  1

0011 ---- NOT  ----  1100

~ 0011           
=> 1100

#################################################

Day.6

(e u */ +-) (shift and or 2) (c not and or)

1. e 
2. u        -, +, ~
3. * / 
4. +-

5. shift
6. and      bitwise
7. xor
8. or

9. c
10. not
11. and
12. 0r

##################################################################################################

Comparison operators(6) (equal, greater)(boolean value)

1. Equal                    ==
2. Not equal                !=
3. Greater than             >
4. Less than                <
5. Greater than or equal    >=
6. Less than or equal       <=

#################################################

Identity operator (2) (id, same object)
- is
- is not

#################################################

Membership operator (2)
- in
- not in

#################################################

Logical operator(3)

1. not       opposite
2. and       all               
3. or        any

#################################################

Ternary operator, Conditional operator, if-else operator
- if else


mark = 80
condition_for_pass = mark >= 40
condition_for_fail = mark < 40

result = "pass" if condition_for_pass else "fail"
print(result)

result2 = "fail" if condition_for_fail else "pass"
print(result2)

#################################################

Assignment operators (13)

1. Normal assign               =

2. Exponent and assign         **=
3. Multiply and assign         *=
4. division and assign         /= 
5. floor division and assign   //=
6. modulus and assign          %= 
7. add and assign              +=
8. substract and assign        -=

9. left shift and assign       <<=
10. right shift and assign     >>=
11. bitwise AND and assign     &= 
12. bitwise XOR and assign     ^= 
13. bitwise OR and assign      |= 

#################################################

Walrus operator ( := )

- operation and assign, assign in operation

##################################################################################################

Small project         100 $       1 months, 1 days
Medium project        500 $               , 1 days
Large scale project              

mind => happy
time => free

>> Money, Novels 

#################################################

Operator တွေကို အုပ်စုခွဲလိုက်ရင် ခုလိုရလာပါမယ်။

Groups of operators (8)

1. Arithmetic Operators(9)
2. Bitwise operators (6)
3. Comparison operators (6)
4. Identity operator (2)
5. Membership operator (2)
6. Logical operator (2)
7. conditional operator(1)
8. assignment operator (14)

ternary လိုမျိုး တစ်ခုတည်းရှိတာကိုတော့ မထည့်ထားပါဘူး။

#################################################

Operand အရေအတွက်နဲ့ အုပ်စုခွဲရင် ခုလိုရလာပါမယ်။

Groups of operators by operands (3)

1. Unary operator   (4)   (+, -, ~, not)
အဆင့်နှစ်က သုံးခုနဲ့ အဆင့် 10 က တစ်ခုနဲ့ဆိုတော့ unary operator 4 ခု ရှိပါမယ်။

2. Binary operator  (38)
43 ထဲက unary 4 ခုနဲ့ ternary 1 ခုကို နှုတ်လိုက်ရင် binary အရေအတွက်ရပါမယ်။

3. Ternary operator (1)

################################################# 

Precedence(15)

1. e 
2. u        -, +, ~
3. * / 
4. +-

5. shift
6. and          bitwise          0011
7. xor
8. or

9. c            c i m
10. not         logical
11. and
12. or

13. t
14. assignment
15. walrus

#################################################

Precedence 15 ခုက ဒါကို အလွတ်ကျက်ရပါမယ်။

(e u */ +-) 
(shift and or 2) 
(c not and or) 
(t assignment walrus)

#################################################

Associativity ကတော့ (e u assign) ကို အလွတ်ကျက်ရပါမယ်။

1.  e, u, assign က right-sided bind ဖြစ်ပါတယ်။
အားလုံးပေါင်းရင် 19 ခု ရှိပါမယ်။ ( 1 + 4 + 14 => 19 )

2. ကျန်တာက left-sided bind ဖြစ်ပါမယ်။ ( 43 - 19 => 24 )

#################################################

အနှစ်ချုပ်

e u မြှောက်စား ပေါင်းနှုတ်
shift and or နှစ်ခု
c not and or
t assignment walrus 


e u assign

#################################################

ဒီအတိုကောက်နှစ်ခုတည်းနဲ့ 
1. Precedence 15
2. Operator 43
3. Associativity(L19, R 24)
4. Groups of operators (8)
5. Groups of operators by operand (3)

ဒီငါးခုလုံးကို ပြန်ပြီး ပုံဖော်နိုင်ရပါမယ်။

##################################################################################################


"""

