"""
  Sample Input:
    "Python Hacktivist 2"
  Sample Output:
    "pYTHON hACKTIVIST 2"
"""

def swap_case(s):
    new_s = ""
    for i in range(len(s)):
        if not s[i].isdigit():
            if s[i].isupper():
                new_s += s[i].lower()
            else:
                new_s += s[i].upper()
        else:
            new_s += s[i]
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
