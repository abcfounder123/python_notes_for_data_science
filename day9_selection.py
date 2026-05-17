
"""
Procedural programming
1. Sequence
2. Selection
3. Loop
4. Function

#################################################

1. Sequence
   - top
   - left
   - parenthesis first

#################################################

2. Selection (if, elif, else)

#####################################

1. if

ချိတ်ဆက်ထားတဲ့ condition မှန်ရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

#####################################

2. else

ချိတ်ဆက်ထားတဲ့ condition မှားရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 40

if c1:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

3. all from all , one from one

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if c2: print("Programmer.")

if c3: print("Engineer.")

if c4: print("Distance.")

#####################################

4. one from all

mark = 400

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if not c1 and c2: print("Programmer.")

if not c1 and not c2 and c3: print("Engineer.")

if not c1 and not c2 and not c3 and c4: print("Distance.")

#####################################

5. one from all by Python ( elif ) ( else + if )

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

#####################################

Programmer  =>  not c1 and c2
Engineer    =>  not c1 and not c2 and c3
Doctor      =>  c1
Distance    =>  not c1 and not c2 and not c3 and c4


Doctor      =>  c1
Programmer  =>  not c1 and c2
Engineer    =>  not c1 and not c2 and c3
Distance    =>  not c1 and not c2 and not c3 and c4

Grade 12    =>  not c1 and not c2 and not c3 and not c4

#####################################

6. if + elif + else

if not c1 and not c2 and not c3 and not c4: print("Grade 12.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

else: print("Grade 12.")

#####################################

A+             90
A              80
B              70
C              50
F

A+  =>  c1
A   =>  not c1 and c2
B   =>  not c1 and c2 and c3
C   =>  not c1 and c2 and not c3 and c4
F   =>  not c1 and c2 and not c3 and not c4

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

#####################################

mark = 100

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

if c1:
    print("A+")

elif c2:
    print("A")

elif c3:
    print("B")

elif c4:
    print("C")

else:
    print("Fail")

##########################################################################

Code quality

A+             90
A              80
B              70
C              50
F

A+  =>  c1
A   =>  not c1 and c2
B   =>  not c1 and c2 and c3
C   =>  not c1 and c2 and not c3 and c4
F   =>  not c1 and c2 and not c3 and not c4

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

#####################################

mark = 100

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

if c1:
    print("A+")

elif c2:
    print("A")

elif c3:
    print("B")

elif c4:
    print("C")

else:
    print("Fail")
    

time = 2 to 8 micro sec
memory = c1 to c4 (120 byte)
    
#####################################

mark = 75

if mark >= 90:
    print("A+")

elif mark >= 80:
    print("A")

elif mark >= 70:
    print("B")

elif mark >= 50:
    print("C")

else:
    print("Fail")

time = 2 to 8 micro sec
memory = 0 to 30 byte

#####################################

mark = 30

if 100 >= mark >= 90:
    print("A+")

if 90 > mark >= 80:
    print("A")

if 80 > mark >= 70:
    print("B")

if 70 > mark >= 50:
    print("C")

if mark < 50:
    print("Fail")
       
#######    

c  => 9
if => 5

time = 14 micro sec
memory = 0 to 30 bytes

####################################################################################

"""

