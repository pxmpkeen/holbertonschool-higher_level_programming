#!/usr/bin/python3
import random
number = -random.randint(-10000, 10000)
#if number < 0:
#    last_digit = -((number * -1) % 10)
#else:
#    last_digit = number % 10
#if last_digit < 6 and last_digit != 0:
#    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
#elif last_digit == 0:
#    print(f"Last digit of {number} is {last_digit} and is 0")
#else:
#    print(f"Last digit of {number} is {last_digit} and is greater than 5")
positive = number
if number < 0:
    positive = number * -1
    last = positive % 10
    if last != 0:
        last = last * -1
else:
    last = positive % 10
if last > 5:
    print("Last digit of {:d} is {:d}".format(number, last), end="")
    print(" and is greater than 5")
elif last < 6 and positive % 10 != 0:
    print("Last digit of {:d} is {:d}".format(number, last), end="")
    print(" and is less than 6 and not 0")
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
