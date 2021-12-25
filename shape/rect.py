from helpers.point import Point
from shape.polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, top, left, width, height):
        points = [
            Point(left, top),
            Point(left + width, top),
            Point(left + width, top+height),
            Point(left, top+height),
        ]
        super().__init__(points, Point(left+width/2, top+width/2))
