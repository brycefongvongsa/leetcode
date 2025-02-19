"""
    link: https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
    Task: You have to write a function that takes two integers as input and outputs their division.
    The function should only output the result in the given range of values, otherwise it should raise an exception.
    The function should handle the following exceptions:
        ZeroDivisionError
        ValueError
    Input Format:
        The first line contains the number of test cases T.
        T lines follow, each containing two integers: a and b
    Sample Input:
        3
        1 0
        2 $
        3 1
    Sample Output:
        Error Code: integer division or modulo by zero
        Error Code: invalid literal for int() with base 10: '$'
        3
"""

for i in range(int(input())):
    try:
      nums = input().split()
      print( int(nums[0]) // int(nums[1]) )
    except ZeroDivisionError as ze:
      print('Error Code:',ze)
    except ValueError as ve:
      print('Error Code:',ve)