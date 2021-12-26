from helpers.point import Point
from helpers.polygon import Polygon


class Triangle(Polygon):
    def __init__(self, top, left, width, height):
        points = [
            Point(left+width/2, top),
            Point(left+width, top+height),
            Point(left, top + height),
        ]
        super().__init__(points, center=Point(left+width/2, top+height/2))