
"""

"abcdefg"

  a  b  c  d  e  f  g 
  0  1  2  3  4  5  6     positive index
 -7 -6 -5 -4 -3 -2 -1     negative index

#################################################

Indexing 

- positive index
- negative index
- hard = total - easy 
- f1, f5, f10
- l1, l5, l10
- middle 
  - odd, m = total // 2
  - even, rm = total // 2, lm = rm - 1

#################################################

Exercise

total = 196

f1 = 0, -196
f5 = 4, -192
f10 = 9, -187

l1 = -1, 195
l5 = -5, 191
l10 = -10, 186

##################################################################################################

Slicing
- value
- index
- start, stop, step

#################################################

Shortcut

- f5 (stop=5)
  => start, f6 
  => start, 5
  => [:5] 

- f10 (stop=10) 
  => start, f11 
  => start, 10 
  => [:10]

- l5 (start=-5)
  => l5, end
  => -5, end
  => [-5:]

- l10 (start=-10)
  => l10, end
  => -10, end
  => [-10:]
  
- reverse => [::-1]
  - left to right  =>  step = +
  - right to left  =>  step = -
  - richest to poorest

#################################################
  
Extra

- half => [:m], [m:] => even(equal), odd(r+1)
- 3    => [:p1], [p1:p2], [p2:]
- 4    => [:p1], [p1:p2], [p2:p3], [p3:]
- 5    => ?

- 75%  => start, 3/4
- 25%  => start, 1/4
- 80%  => start, 4/5
- 20%  => start, 1/5
- 80%, 20% => (start, 4/5), (4/5, end)

#################################################

Knowledge

1. Division
   - True Division
   - Floor Division, Integer Division
   - Modulus

2. Absolute value +1, -1, 1  =>  1

3. length (len)

##################################################################################################

"""
