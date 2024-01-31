#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
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
