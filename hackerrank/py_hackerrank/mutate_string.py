"""
    link: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
    sample input:
        abracadabra
        5 k
    sample output:
        abrackdabra
"""

def mutate_string(string, position, character):
    temp = list(string)
    temp[position] = character
    result = ''.join(temp)
    return result
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)