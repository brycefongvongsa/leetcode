"""
    link: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
    sample input:
        2
        1 2
    sample output:
        3713081631934410656
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))