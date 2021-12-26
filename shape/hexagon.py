from helpers.point import Point
from helpers.polygon import Polygon


class Hexagon(Polygon):
    def __init__(self, top, left, width, height):
        points = [
            Point(left, top + height / 4),
            Point(left + width / 2, top),
            Point(left + width, top + height / 4),
            Point(left + width, top + 3 * height / 4),
            Point(left + width / 2, top + height),
            Point(left, top + 3 * height / 4),
        ]
        super().__init__(points, Point(left+width/2, top+height/2))
