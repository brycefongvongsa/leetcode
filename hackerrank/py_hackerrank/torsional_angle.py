"""
    link: https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true
    You're given four point A, B, C, and D in a 3D Cartesian coordinate system. You're required to print the angle between the plane made by the points A,B,C and B,C,D in degrees(not radians). Let the angle be P H I. The angle should be correct up to 2 decimal places. X.Y means the dot product of X and Y and AB x BC means the cross product of vectors AB and BC. Also AB = B - A.
    Input Format:
        5 8.8 9
        4 -1 3
        7 8.7 3.3
        4.4 5.1 6.3
    Output Format:
        5.69
"""


import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        cross_x = (self.y * no.z) - (self.z * no.y)
        cross_y = (self.z * no.x) - (self.x * no.z)
        cross_z = (self.x * no.y) - (self.y * no.x)
        return Points(cross_x, cross_y, cross_z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))