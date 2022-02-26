# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/25/2022
# Description: A  function named count_letters that takes as a parameter a string and returns a dictionary that tabulates how many of each letter is in that string.
def count_letters(s):
    d = {}
    for ch in s:
        ch = ch.upper()
        if 'A' <= ch <= 'Z':
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
    return d