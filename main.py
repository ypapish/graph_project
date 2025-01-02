from helper import create_window, generate_matrix, to_undirected, print_matrix
from config import WIDTH, HEIGHT, VER_NUM, seed, k, RADIUS
from primitives import get_vertex_closure, draw_vertex, line_connect, loop, arc_connect
import math


def is_opposite(count, i, j):
    half = math.ceil((count - 1) / 2)
    if i > j:
        i, j = j, i
    return i == j - half


def draw_graph_directed(canvas, matrix, radius, screen_width):
    count = len(matrix)
    get_vertex = get_vertex_closure(count, screen_width, radius)
    for i in range(count):
        vertex = get_vertex(i)
        draw_vertex(canvas, vertex)
        for j in range(count):
            if matrix[i][j] == 0:
                continue
            other_vertex = get_vertex(j)
            if i == j:
                loop(canvas, vertex, True)
            elif is_opposite(count, i, j):
                arc_connect(canvas, vertex, other_vertex, True)
            else:
                shift = i > j and matrix[j][i]
                line_connect(canvas, vertex, other_vertex, True, shift)


def draw_graph_undirected(canvas, matrix, radius, screen_width):
    count = len(matrix)
    get_vertex = get_vertex_closure(count, screen_width, radius)
    for i in range(count):
        vertex = get_vertex(i)
        draw_vertex(canvas, vertex)
        for j in range(i + 1):
            if matrix[i][j] == 0:
                continue
            other_vertex = get_vertex(j)
            if i == j:
                loop(canvas, vertex)
            elif is_opposite(count, i, j):
                arc_connect(canvas, vertex, other_vertex)
            else:
                line_connect(canvas, vertex, other_vertex)


def main(canvas,type):
    directed = generate_matrix(VER_NUM, seed, k)
    undirected = to_undirected(directed)
    if type == 1:
        draw_graph_directed(canvas, directed, RADIUS, WIDTH)
        print('Directed Matrix:')
        print_matrix(directed)
    else:
        draw_graph_undirected(canvas, undirected, RADIUS, WIDTH)
        print('Undirected Matrix:')
        print_matrix(undirected)


if __name__ == '__main__':
    window, canvas = create_window('Graph visualization', WIDTH, HEIGHT)
    main(canvas, 1)
    window.mainloop()
