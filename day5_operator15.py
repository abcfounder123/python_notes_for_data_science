
"""

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

(e u */ +-) (shift and or 2)

1. e 
2. u        -, +, ~
3. * / 
4. +-

5. shift
6. and      bitwise
7. xor
8. or

##################################################################################################

"""
