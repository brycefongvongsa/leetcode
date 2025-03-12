"""
    url: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
    In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
    String letters are case-sensitive, so "a" and "A" are different.
"""

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == sub_string[0] and (i + len(sub_string) <= len(string)):
            temp = ""
            for j in range(0, len(sub_string)):
                temp += string[j+i]
                if temp == sub_string and j+1 == len(sub_string):
                  count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)