
"""

Iteration (for)

x = ["apple", "banana", "orange"]

for i in x:
    print(i)

print(x)

#################################################

1. Iterable objects(str, list, ... )
   - iter

2. Iterator
   - next

#################################################

obj + obj      =>   __add__
for i in obj:  =>   __iter__
Access order   =>   __next__

#################################################

representation string     =>   __repr__       return str obj
Iterable objects          =>   __iter__       return iterator obj
Iterator                  =>   __next__       return as you like

#################################################

1. Iterable objects


class X:
    def __iter__(self):
        return iterator_obj


#################################################

2. Iterator


class X:
    def __next__(self):
        return "abc"


#################################################

Iteration process

x = ["apple", "banana", "orange"]

for i in x:
    print(i)

print(x)


for
>> x.iter()         =>  new obj("apple", "banana", "orange")

in
>> next(new obj)    =>  "apple"    =>  new obj("banana", "orange")
>> next(new obj)    =>  "banana"   =>  new obj("orange")
>> next(new obj)    =>  "orange"   =>  new obj()
>> next(new obj)    =>  Error      =>  Stop iteration

#################################################


class X:
    def __init__(self):
        self.data = ["apple", "banana", "orange"]
        self.n = 0

    def __next__(self):
        ans = self.n
        self.n += 1
        return self.data[ans]


a = X()
print(next(a))
print(next(a))
print(next(a))

#################################################

How to stop iteration?

=> raise StopIteration

#################################################

1. "Stop by IndexError"


class L:
    def __init__(self, data):
        self.data = data
        self.n = 0

    def __next__(self):
        ans = self.n
        self.n += 1

        try:
            return self.data[ans]

        except IndexError:
            raise StopIteration


class R:
    def __init__(self, data):
        self.y = data
        self.n = -1

    def __next__(self):
        ans = self.n
        self.n += -1

        try:
            return self.y[ans]

        except IndexError:
            raise StopIteration

#################################################

2. "Stop by condition"

1. Left to Right (If total is 10, maximun positive index is 9.)


class L:
    def __init__(self, data):
        self.data = data
        self.n = 0
        self.max = len(self.data) - 1

    def __next__(self):
        ans = self.n
        self.n += 1

        if ans > self.max:
            raise StopIteration

        return self.data[ans]


2. Right to Left (If total is 10, maximun negative index is -10.)


class R:
    def __init__(self, data):
        self.data = data
        self.n = -1
        self.max = - len(self.data)

    def __next__(self):
        ans = self.n
        self.n += -1

        if ans < self.max:
            raise StopIteration

        return self.data[ans]


#################################################

Changing iteration style of list


                       list      

                        |

                     My_list     new  iter

#################################################


class R:
    def __init__(self, data):
        self.data = data
        self.n = -1
        self.max = - len(self.data)

    def __next__(self):
        ans = self.n
        self.n += -1

        if ans < self.max:
            raise StopIteration

        return self.data[ans]


class MyList(list):
    def __iter__(self):
        return R(self)


x = list(["apple", "banana", "orange"])

for i in x:
    print(i)

print("-" * 42)

y = MyList(["apple", "banana", "orange"])

for i in y:
    print(i)

print("-" * 42)

#################################################

Adding iteration to int


                       int      

                        |

                      Myint      iter
                     

class L:
    def __init__(self, data):
        self.data = data
        self.n = 0
        self.max = len(data) - 1

    def __next__(self):
        ans = self.n
        self.n += 1
        if ans > self.max:
            raise StopIteration
        return self.data[ans]


class Myint(int):
    def __iter__(self):
        return L(str(self))


x = Myint(1500)

for i in x:
    print(i)

#################################################

Creating Iterable objects   =>  __iter__()


class Z:
    def __init__(self):
        self.data1 = ["apple", "banana", "orange", "mangoes",  "orange", "mangoes", "apple", "banana",]
        self.data2 = "123456"
        self.data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __iter__(self):
        return L(self.data3)


x = Z()

for i in x:
    print(i)

#################################################

"Test"


class L:
    def __init__(self, data):
        self.data = data
        self.n = 0
        self.max = len(self.data) - 1

    def __next__(self):
        ans = self.n
        self.n += 1

        if ans > self.max:
            raise StopIteration

        return self.data[ans]


class R:
    def __init__(self, data):
        self.data = data
        self.n = -1
        self.max = - len(self.data)

    def __next__(self):
        ans = self.n
        self.n += -1

        if ans < self.max:
            raise StopIteration

        return self.data[ans]


class Z:
    def __init__(self):
        self.data1 = ["apple", "banana", "orange", "mangoes",  "orange", "mangoes", "apple", "banana",]
        self.data2 = "123456"
        self.data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __iter__(self):
        return L(self.data3)


x = Z()

for i in x:
    print(i)

##################################################################################################

Brainstorm exercise => Quarter 1/4

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[1, 2, 3] [4, 5, 6] [7, 8, 9] [10, 11, 12]

>> [start: p1], [p1: p2], [p2: p3], [p3: end]


class Quarter:
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.p1 = len(data) // 4     # p1 = t // 4
        self.end = self.p1
        self.n = 0
        self.f = 2

    def __next__(self):
        self.n += 1

        start = self.start            # [start: p1]
        end = self.end                # [0: p1]

        self.start = self.end         # prepare for next [p1: p2]
        self.end = self.p1 * self.f   # p2 = p1 * 2 , p3 = p1 * 3

        self.f += 1

        if self.n == 5:
            raise StopIteration

        return self.data[start: end]


#################################################

"Test"


class Quarter:
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.p1 = len(data) // 4     # p1 = t // 4
        self.end = self.p1
        self.n = 0
        self.f = 2

    def __next__(self):
        self.n += 1

        start = self.start            # [start: p1]
        end = self.end                # [0: p1]

        self.start = self.end         # prepare for next [p1: p2]
        self.end = self.p1 * self.f   # p2 = p1 * 2 , p3 = p1 * 3

        self.f += 1

        if self.n == 5:
            raise StopIteration

        return self.data[start: end]


class Z:
    def __init__(self):
        self.data1 = ["apple", "banana", "orange", "mangoes",  "orange", "mangoes", "apple", "banana",]
        self.data2 = "123456"
        self.data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def __iter__(self):
        return Quarter(self.data3)


x = Z()

for i in x:
    print(i)

#################################################

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[10, 11, 12]

##################################################################################################

"""
