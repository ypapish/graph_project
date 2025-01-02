import tkinter as tk
import random
import math

def create_window(title, width, height):
    window = tk.Tk()
    window.geometry(f'{width}x{height}')
    window.title(title)
    canvas = tk.Canvas(window, borderwidth=0, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=1)
    return window, canvas


def print_matrix(matrix):
    for row in matrix:
        for n in row:
            print(n, end = ' ')
        print()


def generate_matrix(size, seed, k):
    random.seed(seed)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            rand = random.random() * 2
            val = math.floor(rand * k)
            row.append(val)
        matrix.append(row)
    return matrix


def to_undirected(matrix):
    length = len(matrix)
    result = []
    for i in range(length):
        row = []
        for j in range(length):
            if matrix[i][j] or matrix[j][i]:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result