#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    sum = 0
    prev = 1000
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        curr = nums[roman_string[i]]
        if i < len(roman_string) - 1:
            next = nums[roman_string[i + 1]]
            if next > curr:
                sum -= 2 * curr
        sum += curr
    return sum



roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
