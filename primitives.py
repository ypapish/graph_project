from math import atan2, pi, sin, cos, sqrt
from config import RADIUS, arrowshape


class Vertex:
    def __init__(self, x, y, name):
      self.x = x
      self.y = y
      self.name = name
