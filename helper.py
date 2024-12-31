import tkinter as tk


def create_window(title, width, height):
    window = tk.Tk()
    window.geometry(f'{width}x{height}')
    window.title(title)
    canvas = tk.Canvas(window, borderwidth=0, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=1)
    return window, canvas
