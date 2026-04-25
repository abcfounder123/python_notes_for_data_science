
"""

1. Data Types of Python (13 + 2)

1. str()

2. int()
3. float()
4. complex()

5. list()
6. tuple()
7. set()
8. frozenset()
9. bytearray()
10. bytes()
11. range()
12. dict()

13. bool()

14. memoryview()
15. NoneType

#################################################

2. Creating data types by Names (14)

1. str()
2. int()
3. float()
4. complex()
5. list()
6. tuple()
7. set()
8. frozenset()
9. bytearray()
10. bytes()
11. range()
12. dict()
13. bool()
14. memoryview()

#################################################

1 + 2                        <-- Creating data types by Symbols

int(1).__add__(int(2))       <-- Creating data types by Names

#################################################

3. Creating data types by Symbols (11)

1. quotes
2. .          decimal point
3. j
4. [ ]        square bracket
5. ( )        round bracket
6. { }        curly bracket
7. b
8. { }

Vlaue is symbol.
1. integer   =>  1
2. boolean   =>  True False
3. NoneType  =>  None

#################################################

4. Name only

1. frozenset()
2. bytearray()
3. range()
4. memoryview()

##################################################################################################

Knowledge

1. exponent(e6)(10 ** 6)

2. float value 
   - round

3. collection, element

4. empty 
   - 0, 0.0, 0j   => empty value
   - [], (),  {}  => empty elements

5. tuple with single element     
   - comma 
   - (1,), ("Mg Mg",)

6. range
   - start, stop, step
   - shortcut
     - range(0, 10, 1)
     - range(0, 10)
     - range(10)

7. dict
   - items
   - keys
   - values

8. dict or set
   - {}  =>  dict

9. Empty set(by name)
   - {}     <--- X
   - set()

#################################################


"""

# Checking data type

b''
b'apple'

bytearray(b'')
bytearray(b'apple')

memoryview(b"apple")
# <memory at 0x1005f2080>

''
' '
'1000'
"1000"
'''1000'''
"""1000"""

0j
3 + 2j
1j
complex(3, 2)

0
-1
+1
1_000
1_000_000
1_000_000_000
1000000000

0.0
-1.0
+1.0
1.0
1000.0
.01
100.
0.
.0
1_000_000.0
1e6  # e6 = 1000000

1e9

1000000000000.0
1_000_000_000_000.0
1e12


1e-1  # e-1 = 1/10 = 0.1
1e-2  # e-2 = 1/100 = 0.01
1e-6  # e-6 = 1/1000000 = 0.000001
0.000001
1e-9  # 0.000000001
1.234e-9  # 0.000000001234

# correct answer = 0.0, 159e-15 => 0.00000000000000159
0.00
0.000
0.000000

# 0.0  => rocket
# 0.000000000000001 => round => 0.00

["apple", "banana", "orange"]
[]
list()

()
tuple()
"Mg Mg", 20, 5.5
("Mg Mg", 20, 5.5)
(1, )
("Mg Mg", )

("Mg Mg")  # "Mg Mg"
(1)  # 1

range(0, 10, 1)
range(0, 10)
range(10)
range(2, 101, 2)

{"name": "Mg Mg", "age": 20, "height": 5.5}

{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5,
    "marks": [60, 70, 80]
}

{}

{"apple", "banana", "orange"}
set()
frozenset()
frozenset({'apple', 'orange', 'banana'})  # frozenset
frozenset(['apple', 'orange', 'banana'])
frozenset(('apple', 'orange', 'banana'))

1000
0
int()

True
False
bool()

None

{}
dict()
set()
{1, }

"1000"
str(1000)

1000
int("1000")

1000.0
float(1000)
float("1000")



