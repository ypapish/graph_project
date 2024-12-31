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


def get_coord(x, y, dist, angle):
    x1 = x + dist * cos(angle)
    y1 = y + dist * sin(angle)
    return x1, y1


def get_vertex_closure(count, size, radius):
    x_center, y_center = size / 2, size / 2
    length = size / 2 - 1.3 * radius
    step = 2 * pi / (count - 1)
    def get_vertex(index):
      if index == 0:
        return Vertex(size / 2, size / 2, 0)
      angle = (index - 1) * step
      x, y = get_coord(x_center, y_center, length, angle)
      return Vertex(x, y, index)
    return get_vertex
