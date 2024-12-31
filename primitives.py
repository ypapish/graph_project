from math import atan2, pi, sin, cos, sqrt
from config import RADIUS, arrowshape


class Vertex:
    def __init__(self, x, y, name):
      self.x = x
      self.y = y
      self.name = name


def draw_circle(canvas, x, y):
    x1, y1 = x - RADIUS, y - RADIUS
    x2, y2 = x + RADIUS, y + RADIUS
    canvas.create_oval(x1, y1, x2, y2, width=2,fill="pink",outline="pink")


def draw_vertex(canvas, vertex):
    x, y = vertex.x, vertex.y
    draw_circle(canvas, x, y)
    canvas.create_text(x, y, text=vertex.name, font=5)
