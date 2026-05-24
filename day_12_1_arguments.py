
"""

Arguments

value passed by function        <--   argument
other value                     <--   value

##########################################

Arguments(7)

1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Positional only arguments
5. Keyword only arguments
6. Arbitrary positional arguments
7. Arbitrary keyword arguments

##########################################

Positional arguments                  No.1
Positional only arguments             No.3
Arbitrary positional arguments        No.5

##########################################


def add(a, b, z=0):  <---   3. default argument
    pass

add(1, 2)            <---   1. positional argument
add(a=1, b=2)        <---   2. keyword argument


def add(a, b, /):
    pass

add(1, 2)            <---   4. positional only argument


def add(*, a, b):
    pass

add(a=1, b=2)        <---   5. keyword only argument


def add(*x):
    pass

add(1)
add(1, 2)
add(1, 2, 3)         <---   6. arbitrary positional argument


def add(**x):
    pass

add(x=1)
add(x=1, y=2)
add(x=1, y=2, z=3)   <---   7. arbitrary keyword argument

##########################################

Arbitrary keyword arguments      (x=1, y=2, z=3)         ?   =>  6. (**kwargs)
Arbitrary positional arguments   (1, 2, 3)               ?   =>  5. (*args)
Positional arguments             (1, 2)                  ?   =>  1. (a, b)
Keyword arguments                (a=1, b=2)              ?   =>  1. (a, b)
Positional only arguments        (1, 2)                  ?   =>  3. (a, b, /)
Keyword only arguments           (a=1, b=2)              ?   =>  4. (*, a, b)
default argument                                         ?   =>  parameter list

##########################################

"""
