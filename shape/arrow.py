from shape.point import Point
from shape.polygon import Polygon


class Arrow(Polygon):
    def __init__(self, top, left, width, height):
        points = [
            Point(left+width/2, top),
            Point(left+width, top+height/3),
            Point(left+3*width/4, top+height),
            Point(left+width/4, top+height),
            Point(left, top + height / 3),
        ]
        super().__init__(points, center=Point(left+width/2, top))