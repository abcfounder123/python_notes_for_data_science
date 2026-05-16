
"""

Selection

1. Normal Statement ( ; end of line)
   - motor on
   - motor off
   - pass
   - fail

2. Conditional Statement
   - If water level is low, motor on.  
   - If water level is high, motor off. 
   - if exam pass, show "pass".
   - if exam fail, show "fail".

3. Conditional if Statement
   - boolean data type
   - True

3. Conditional else Statement
   - boolean data type
   - False
   
################################################

1. Conditional if, if
2. Code block
3. Conditional code block
4. Conditional if code block, if code block, if block 
5. Conditional else code block, else code block, else block  
6. Condition
7. Boolean value
   - empty => False
   - any   => True
8. program flow
9. control flow
10. : (code block)
11. pass (keyword name for pass)

################################################

8. program flow

1. input
2. assign
3. input
4. assign
5. if
6. l eq
7. r eq
8. and
9. print

username = input("username = ")
password = input("password = ")
if username == "Mg Mg" and password == "12345": print("login successful.")

################################################

Nested if (step.4)

Step.1 (condition => output?) (flow)

- 1010 => adgi
- 1010 => adgj

################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 0

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        if c3:
            print("g")
            if c4:
                print("i")
            else:
                print("j")
        else:
            print("h")

else:
    print("b")
    if c3:
        print("e")
    else:
        print("f")

################################################

Step.2 (output => condition?) (control)

print("Apple.1")  => 1011
print("Apple.2")  => 1010
print("Apple.3")  => 100-
print("Apple.4")  => 10--
print("Apple.5")  => 0-1-
print("Apple.5")  => 0-0-

################################################

c1 = 0
c2 = 0
c3 = 1
c4 = 0

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        print("Apple.4")
        if c3:
            print("g")
            if c4:
                print("i")
                print("Apple.1")
            else:
                print("j")
                print("Apple.2")
        else:
            print("h")
            print("Apple.3")
else:
    print("b")
    if c3:
        print("e")
        print("Apple.5")
    else:
        print("f")
        print("Apple.6")

################################################

Step.3 (condition => new code)

101   =>   print("new.1")
100   =>   print("new.2")
0-1   =>   print("new.3")
0-0   =>   print("new.4")

111   =>   print("new.5")
110   =>   print("new.6")

011   =>   print("new.7")
00-   =>   print("new.8")
010   =>   print("new.9")

################################################

if c3:
    print("new.5")
    
else:
    print("new.6")
    
    
if c2:
    if c3:
        print("new.7")
        
################################################  
              
c1 = 0
c2 = 1
c3 = 0
c4 = 1

if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("new.5")
        else:
            print("new.6")
    else:
        print("d")
        if c3:
            print("new.1")
            print("g")
            if c4:
                print("i")
            else:
                print("j")
        else:
            print("new.2")
            print("h")
else:
    if c2:
        if c3:
            print("new.7")
        else:
            print("new.9")
    else:
        print("new.8")
    print("b")
    if c3:
        print("new.3")
        print("e")
    else:
        print("new.4")
        print("f")

################################################

Step.4 ( idea => code )

1. low level

if low_level:
    print("motor on.")

################################################

2. electric, not electric

if low_level:
    if electric:
        print("motor on.")
    else:
        print("generator on.")
        print("motor on.")

################################################

3. short circuit, not short circuit


if short_circuit:
    print("call mechanic for m1")
else:
    print("motor on.")

################################################

110
low_level + electric + not short circuit   => print("motor on.")

100
low_level + not electric + not short circuit   => print("motor on.")


111
low_level + electric + short circuit   => print("call mechanic for m1")

101
low_level + not electric + short circuit   => print("call mechanic for m1")


10    =>   print("generator on.")
101   =>   print("generator off.")

################################################

low_level = 1
electric = 0
short_circuit = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            print("generator off.")
        else:
            print("motor on.")

################################################

4. motor.2

111
low_level + electric + short_circuit  => print("motor.2 on")

101
low_level + not electric + short_circuit  => print("motor.2 on")

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            print("motor.2 on")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            print("motor.2 on")
        else:
            print("motor on.")

################################################

5. short_circuit2, not short_circuit2


if short_circuit2:
    print("call mechanic for m2")
else:
    print("motor.2 on")
    
################################################
 
low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
            else:
                print("motor.2 on")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                print("generator off.")
            else:
                print("motor.2 on")
        else:
            print("motor on.")
     
################################################

6. motor.3

1111
low_level + electric + short_circuit + short_circuit2 => print("motor.3 on")

1011
low_level + not electric + short_circuit + short_circuit2  => print("motor.3 on")

################################################

low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                print("motor.3 on")
            else:
                print("motor.2 on")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                print("motor.3 on")
            else:
                print("motor.2 on")
        else:
            print("motor on.")

################################################################################################

7. short_circuit3, not short_circuit3


if short_circuit3:
    print("call mechanic for m3")
else:
    print("motor.3 on")
    
################################################

8. motor.4

11111
low_level + electric + short_circuit + short_circuit2 + short_circuit3 => print("motor.4 on")

10111
low_level + not electric + short_circuit + short_circuit2 + short_circuit3 => print("motor.4 on")


################################################

9. short_circuit4, not short_circuit4


if short_circuit4:
    print("call mechanic for m4")
else:
    print("motor.4 on")
     
################################################

low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1
short_circuit3 = 0

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                else:
                    print("motor.3 on")
            else:
                print("motor.2 on")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                    print("generator off.")
                else:
                    print("motor.3 on")
            else:
                print("motor.2 on")
        else:
            print("motor on.")

################################################################################################

"""

