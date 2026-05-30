
"""

Function (10)

1. Introduction
   - print(), input(), len(), int(input())
   - Function call =>  print, print()
   - Why?
     - Readability, reuse
     - Decomposition
   - Where?
     1. built-in module
     2. preinstalled module  tkinter.py, math.py, .....
     3. external module      PyQt5, numpy
     4. custom function

2. module, package, framwork
   - function (collection of program)         (one purpose - add(), sqrt() )
   - module   (file)   (collection of fun)    (one work - math.py, login.py)
   - package  (folder) (collection of module) (one group - frontend folder)
   - framework(folder) (collection of package)(one project - Django)

3. Function name
   - naming rules
   - same name (last one)
   - should not give the same name

4. Parameterized function
   - parameterized function   => def add(x, y):
   - parameter list           => (x, y), tuple
   - first parameter          => x

5. Arguments(7)
   - value passed by function
   - positional argument  =>  add(1, 2)
   - keyword argument     =>  add(x=1, y=2)
   - ...

6. Local, Global, Built-in
   Local          => local
   Global         => all (local file)
   Built-in       => all file

7. Standrd form(3)

8. Types of parameters(6)

9. Passing correct values to function

10. Checking Parameters

##########################################

Decomposition

     .    .
   X .    .  
 ----------------
     . X  .  
 ----------------
     .    .  X
     .    .


Board
draw X
draw O
check win
check tie
marks

##########################################

Passing correct values to function

a = 20
b = 10
c = 30
args = (1000, 700, 1100)
user_name = "Mg Mg"
password  = "12345"
kw        = {country: "Myanmar", "age": 10}


a, b, c,                pos
*args                   all pos
user_name, password     keyword
**kw                    all items


def f(a, b, c, /, *args, user_name, password, **kw):
    print(a, b, c)
    print(args)
    print(user_name, password)
    print(kw)


f(20, 10, 30, 1000, 700, 1100, user_name="Mg Mg", password="12345", country="Myanmar", age=10)

##########################################

Checking Parameters

No.5 + No.2
help(print)   =>   def print(*args, sep=' ', end='\n', file=None, flush=False):

No.2 + No.3
help(input)   =>   def input(prompt='', /):

No.3
help(len)     =>   def len(obj, /):

####################################################################################

"""
