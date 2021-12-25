from math import pi


class Degree:
    def __init__(self, degree):
        self.degree = (degree+pi)%(2*pi)-pi
        self.d = self.degree
    def __add__(self, other):
        if isinstance(other, Degree):
            return Degree(self.degree + other.degree)
        else:
            return Degree(self.degree + other)
    def __sub__(self, other):
        if isinstance(other, Degree):
            return Degree(self.degree - other.degree)
        else:
            return Degree(self.degree - other)

    def __mul__(self, other):
        if isinstance(other, Degree):
            return Degree(self.degree * other.degree)
        else:
            return Degree(self.degree * other)