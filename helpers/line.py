from helpers.point import Point


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.p1 = point1
        self.p2 = point2
        self.points = [point1, point2]
        self.edge = self.p1-self.p2

    def normal(self):
        return Point(-self.edge.y, self.edge.x)