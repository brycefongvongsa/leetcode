"""
    url: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
    Python has built-in string validation methods for basic data. 
    In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if s has any alphabetical characters. Otherwise, print False.
    In the third line, print True if s has any digits. Otherwise, print False.
    In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
"""

if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))