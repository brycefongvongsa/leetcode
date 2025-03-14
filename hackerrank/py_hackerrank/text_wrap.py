"""
    url: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
    You are given a string s and width w. Your task is to wrap the string into a paragraph of width w.
    Sample Input:
    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4
    
    Sample Output:
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ
    
"""

import textwrap

def wrap(string, max_width):
    result = ""
    string_list = textwrap.wrap(string, max_width)
    for i in string_list:
      result += i + "\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)