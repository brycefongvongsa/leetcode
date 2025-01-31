"""
    link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
    
    The first line contains . The second line contains an array   of  integers each separated by a space.
    
    Sample Input: 
        5
        2 3 6 6 5
    Sample Output:
        5
"""

if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))
    ## create a new list. set() removes duplicates
    result = list(set(arr))
    ## get second to last value of list
    print(result[len(result)-2])
    