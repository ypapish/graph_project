from helper import create_window, generate_matrix, to_undirected, print_matrix
from config import WIDTH, HEIGHT, VER_NUM, seed, k, RADIUS
from primitives import get_vertex_closure, draw_vertex, line_connect, loop, arc_connect
import math


def is_opposite(count, i, j):
  half = math.ceil((count - 1) / 2)
  if i > j: (i, j) = (j, i)
  return i == j - half

