"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
    string_list = [str(i) for i in n]
    
    s1 = ""
    n1 = string_list[:3]
    for i in n1:
        s1 += str(i)
        
    s2 = ""
    n2 = string_list[3:6]
    for i in n2:
        s2 += str(i)
    s3 = ""
    n3 = string_list[6:10]
    for i in n3:
        s3 += str(i)
        
    return f'({s1}) {s2}-{s3}'
