
"""
 
1. Arithmetic Operators(9)  (e u */ +-)

1. exponent        **
2. negative        -
3. positive        +
4. multiplication  *
5. true division   /       2.5
6. floor division  //      2
7. modulus         %       1
8. addition        +
9. substraction    -

Exercises of Arithmetic Operators

1. age = 2026 - Birth year , "You are 26 years old."
2. kyats to dollar, "10000 kyats is equal to 2 dollars."
3. 350 seconds is equal to 5 minutes and 50 seconds.
4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.
5. Half-life calculator

##########################################

1. print, seperator = " ", end = "\n", file, flash
2. input, prompt letter
3. TypeCasting (int, str, .. )
4. String concatination  (+)
5. string formatting => f, {}

##########################################

1. age = 2026 - Birth year , "You are 26 years old."

x = input("Birth year = ")
age = 2026 - int(x)
ans = "You are " + str(age) + " years old."
print(ans)

##########################################

2. kyats to dollar, "10000 kyats is equal to 2 dollars."

kyat = int(input("Kyats = "))
dollar = kyat / 5000
ans = str(kyat) + " kyats is equal to " + str(dollar) + " dollars."
print(ans)

##########################################

3. 350 seconds is equal to 5 minutes and 50 seconds.

total_second = int(input("Seconds = "))
minute = total_second // 60
second = total_second % 60
ans = str(total_second) + " seconds is equal to " + str(minute) + " minutes and " + str(second) + " seconds."
print(ans)

total_seconds = int(input("Total seconds = "))
minutes = total_seconds // 60
seconds = total_seconds % 60
ans = f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds."
print(ans)

##########################################

4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.

                   90350  seconds

                 1505 min  +   50 sec

               25 hour + 5 min

             1 day + 1 hour

total_second = int(input("Seconds = "))

total_minute = total_second // 60
second = total_second % 60

total_hour = total_minute // 60
minute = total_minute % 60

day = total_hour // 24
hour = total_hour % 24

ans = f"{total_second} seconds is equal to {day} days {hour} hours {minute} minutes and {second} seconds."

print(ans)

##########################################

5. Half-life calculator

Half-life = 6 months

                       500  g

                       250  g       6

                       125  g       6

                       62.5 g       6

500 / 2 / 2 / 2
500 * 0.5 * 0.5 * 0.5
500 * 0.5 ** 3

w = float(input("Weight = "))
h = float(input("Half-life in year = "))
time = float(input("Year = "))

count = time / h
ans = w * 0.5 ** count

print(ans)

####################################################################################

"""
