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
    canvas.create_oval(x1, y1, x2, y2, width=2, fill="pink", outline="pink")


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


def line_connect(canvas, ver1, ver2, arrows=False, shift=False):
    x1, y1 = ver1.x, ver1.y
    x2, y2 = ver2.x, ver2.y
    fi = atan2(y2 - y1, x2 - x1)
    angle1 = fi
    angle2 = fi + pi
    if shift:
        angle1 -= pi / 8
        angle2 += pi / 8
    x3, y3 = get_coord(x1, y1, RADIUS, angle1)
    x4, y4 = get_coord(x2, y2, RADIUS, angle2)
    options = {
      'width': 2,
      'arrowshape': arrowshape,
    }
    if arrows:
        options['arrow'] = 'last'
    canvas.create_line(x3, y3, x4, y4, options)


def arc_connect(canvas, ver1, ver2, arrows=False):
    fi = atan2(ver2.y - ver1.y, ver2.x - ver1.x)
    x3, y3 = get_coord(ver1.x, ver1.y, RADIUS, fi - pi / 8)
    x4, y4 = get_coord(ver2.x, ver2.y, RADIUS, fi + pi  + pi / 8)
    meadle = sqrt((x4 - x3)**2 + (y4 - y3)**2) / 2
    length = sqrt((2 * RADIUS)**2 + meadle**2)
    angle = -atan2(2 * RADIUS, meadle)
    x5, y5 = get_coord(x3, y3, length, angle + fi)
    options = {
      'width': 2,
      'arrowshape': arrowshape,
      'smooth': True
    }
    if arrows:
        options['arrow'] = 'last'
    canvas.create_line(x3, y3, x5, y5, x4, y4, options)


def loop(canvas, vertex, arrows=False):
    x, y = vertex.x, vertex.y + RADIUS
    x1, y1 = get_coord(x, y, RADIUS, 3 * pi / 4 - pi / 2)
    x2, y2 = get_coord(x, y, RADIUS, -3 * pi / 4 - pi / 2)
    options = {
      'width': 2,
      'arrowshape': arrowshape,
    }
    if arrows:
        options['arrow'] = 'last'
    canvas.create_line(x, y, x1, y1, x2, y2, x, y, options)
    
