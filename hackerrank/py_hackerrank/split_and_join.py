"""
  Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
  Sample Input: 
    this is a string
  Sample Output:
    this-is-a-string
"""

def split_and_join(line):
    # write your code here
    s = line.split(" ")
    s = "-".join(s)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
