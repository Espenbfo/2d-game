from typing import List, Tuple

import pygame.draw
from pygame.surface import Surface

from config import WINDOW_SIZE
from helpers.degree import Degree
from helpers.line import Line
from helpers.point import Point


class Polygon:
    def __init__(self, points: List[Point], center: Point):
        self.points = points
        self.raw_points = [(point.x, point.y) for point in points]
        self.edge_count = len(points)
        self.center = center

        self.rotation = Degree(0)
        self.displacement = Point(0, 0)
        self.scaling = 1

    def edge(self, index):
        point1 = self.points[index]
        if index != self.edge_count - 1:
            point2 = self.points[index + 1]
        else:
            point2 = self.points[0]
        return Line(point1, point2)

    def project(self, axis: Point):
        min_product = 100000
        max_product = -100000
        for point in self.points:
            dot_product = point.dot(axis)
            if dot_product < min_product:
                min_product = dot_product
            elif dot_product > max_product:
                max_product = dot_product
        return min_product, max_product

    @staticmethod
    def interval_distance(min_a, max_a, min_b, max_b):
        if min_a < min_b:
            return min_b - max_a
        else:
            return min_a - max_b

    def collide(self, other):

        for i in range(self.edge_count + other.edge_count):
            if i < self.edge_count:
                edge = self.edge(i)
            else:
                edge = other.edge(i - self.edge_count)

            normal = edge.normal()

            min_a, max_a = self.project(normal)
            min_b, max_b = other.project(normal)

            if Polygon.interval_distance(min_a, max_a, min_b, max_b) > 0:
                return False
        return True

    def display(self, screen: Surface, color: Tuple[int, int, int]):
        pygame.draw.polygon(screen, color, self.raw_points)

    def scale(self, factor):
        self.scaling *= factor

    def rotate(self, degree):
        self.rotation += degree

    def move(self, x, y, limit=WINDOW_SIZE):

        points = []
        if self.scaling != 1 or self.rotation:
            for index, point in enumerate(self.points):
                point = point.rotate_around(self.center, -(self.rotation.degree))

                points.append((self.center - point) * self.scaling)
        else:
            points = self.points
        polygon = Polygon(points, self.center)

        if limit:
            surrounding_rect = polygon.surrounding_rect()
            box_x, box_y, width, height = surrounding_rect
            lim_x, lim_y = limit
            new_x = box_x + x + self.displacement.x
            new_y = box_y + y + self.displacement.y
            if new_x < 0:
                x = x - new_x
            elif new_x + width > lim_x:
                x = lim_x - (box_x + self.displacement.x + width)
            if new_y < 0:
                y = y - new_y
            elif new_y + height > lim_y:
                y = lim_y - (box_y + self.displacement.y + height)

        displacer = Point(x, y) + self.displacement
        points = []
        for i, point in enumerate(polygon.points):
            points.append(point + displacer)
        new_center = self.displacement
        self.displacement = displacer
        return Polygon(points, new_center)

    def surrounding_rect(self):
        min_x = float("inf")
        min_y = float("inf")
        max_x = -float("inf")
        max_y = -float("inf")
        for point in self.points:
            x, y = point.pos
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
        return min_x, min_y, max_x - min_x, max_y - min_y

    def outside_bounds(self, bounds=WINDOW_SIZE):
        surrounding_rect = self.surrounding_rect()
        box_x, box_y, width, height = surrounding_rect
        lim_x, lim_y = bounds
        x = box_x + self.displacement.x
        y = box_y + self.displacement.y
        if x + width < 0:
            return True
        if x > lim_x:
            return True
        if y < width:
            return True
        if y > lim_y:
            return True
        return False

    def __copy__(self):
        p = Polygon(self.points, self.center)
        p.rotation = self.rotation
        p.scaling = self.scaling
        p.displacement = self.displacement.__copy__()
        return p