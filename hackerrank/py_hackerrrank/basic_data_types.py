"""
    Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
    
    Example
    marks key: value pairs are
    'alpha' : [20, 30, 40]
    'beta' : [30, 50, 70]
    query_name = 'beta'
    The query_name is 'beta'. beta key has value [30, 50, 70] which contains the marks 50. So the output is 50.
    
    sample input:
        3
        alpha 20 30 40
        beta 30 50 70
        gamma 50 60 80
        beta
    sample output:
        56.00
"""

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     average_score = float(0.00)
#     sum_score = 0
#     for i in student_marks[query_name]:
#       sum_score += i
#     average_score = format(sum_score/len(student_marks[query_name]), '.2f')
#     print(average_score)