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
