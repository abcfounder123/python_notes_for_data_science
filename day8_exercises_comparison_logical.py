
"""

Comparison Operators(6) (True, False)

1. equal                   ==
2. not equal               !=
3. greater than            >
4. less than               <
5. greater than or equal   >=
6. less than or equal      <=

##########################################

Exercises of Comparison Operators

1. If mark is greater than or equal to 40, exam pass.
2. If mark is less than 40, exam fail.
3. If mark is greater than or equal to 40, exam pass.
Else, exam fail.
4. one from one (if)
5. one from two (if + else)

##########################################

1. If mark is greater than or equal to 40, exam pass.

if mark >= 40: print("exam pass")

##########################################

2. If mark is less than 40, exam fail.

if mark < 40: print("exam fail")

##########################################

3. If mark is greater than or equal to 40, exam pass.
Else, exam fail.

if mark >= 40: print("exam pass")
else: print("exam fails")

##########################################

4. one from one

mark = int(input("Mark = "))
if mark >= 40: print("exam pass")
if mark < 40: print("exam fail")

##########################################

5. one from two

mark = int(input("Mark = "))
if mark >= 40: print("exam pass")
else: print("exam fails")

####################################################################################

Logical Operators (3) (logical value, boolean value) (True, False)

1. not   =>  opposite
2. and   =>  all
3. or    =>  any

Exercises of Logical Operators

1. If mark is greater than 40 or mark is equal to 40, exam pass.                          or
2. if video lesson class or zoom lesson class, Kaggle course. 
3. If username is equal to "Mg Mg" and password is equal to "12345", login successful.    and
4. if full water, Motor Stop.
5. if not full water, Motor ON.                                                           not

####################################################################################

1. If mark is greater than 40 or mark is equal to 40, exam pass.

if mark > 40 or mark == 40: print("exam pass")

##########################################

2. If video lesson class or zoom lesson class, Kaggle course. 

if video_lesson_class or zoom_class: print("Kaggle course. ")

##########################################

3. If username is equal to "Mg Mg" and password is equal to "12345", login successful.

if username == "Mg Mg" and password == "12345": print("login successful.")

##########################################

4. if full water, Motor Stop.

if full_water: print("Motor Stop.")

##########################################

5. if not full water, Motor ON.

if not full_water: print("Motor On.")

####################################################################################

"""
