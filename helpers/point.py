from math import sqrt, cos, sin


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x-other.x, self.y-other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x*other.x, self.y*other.y)
        else:
            return Point(self.x * other, self.y * other)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def __abs__(self):
        return sqrt(self.x**2+self.y**2)

    def normalized(self):
        length = abs(self)
        return Point(self.x/(length+0.0001), self.y/(length+0.0001))

    def __str__(self):
        return "x: " + str(self.x) + " | y: " + str(self.y)

    def rotate_around(self, point, angle):
        origin_point = self - point
        c = cos(angle)
        s = sin(angle)
        rotated = Point(origin_point.x*c-origin_point.y*s, origin_point.x*s+origin_point.y*c)
        return rotated + point

    def __copy__(self):
        return Point(self.x ,self.y)