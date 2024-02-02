import datetime
import math
import random
from math import cos, pi, sin

from PIL import Image, ImageDraw

BLUE = (68, 114, 196)
GRAY = (128, 128, 128)
MARGIN = 0


def scatter_plot_int(input, scale=1):
    timestamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H%M%S%f")

    x_min, x_max = input[0][0], input[0][0]
    y_min, y_max = input[0][1], input[0][1]

    for i in input:
        x, y = i[0], i[1]
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y

    # print(x_min, x_max, y_min, y_max)

    width, height = (x_max - x_min + 1), (y_max - y_min + 1)
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    adjusted_input = []
    for i in input:
        adjusted_input.append((i[0] - x_min, (i[1] - y_max) * -1))

    adjusted_input = tuple(adjusted_input)

    draw.line(((0, abs(y_max)), (width, abs(y_max))), GRAY)
    draw.line(((abs(x_min), 0), ((abs(x_min), height))), GRAY)
    draw.point(adjusted_input, fill=BLUE)

    image = image.resize((width * scale, height * scale), Image.NEAREST)
    image.save(f"./outputs/result_{timestamp}.png")
    # image.show()


def convert_float_to_int(input, digit):
    adjusted_input = []
    for i in input:
        adjusted_input.append(
            (round(i[0] * 10 ** (digit - 1)), round(i[1] * 10 ** (digit - 1)))
        )

    return adjusted_input


def Astroid():
    points = []
    t = 0
    while t <= pi * 2:
        points.append((cos(t) ** 3, sin(t) ** 3))
        t += 0.0001 * pi

    return convert_float_to_int(points, 3)


def Cardioid():
    points = []
    t = 0
    while t <= pi * 2:
        points.append(((1 + cos(t)) * cos(t), (1 + cos(t)) * sin(t)))
        t += 0.0001 * pi

    return convert_float_to_int(points, 3)


def Cycle():
    points = []
    t = 0
    while t <= pi * 2:
        points.append((cos(t), sin(t)))
        t += 0.0001 * pi

    return convert_float_to_int(points, 3)


def Cycloid():
    points = []
    t = 0
    while t <= pi * 2:
        points.append((t - sin(t), 1 - cos(t)))
        t += 0.0001 * pi

    return convert_float_to_int(points, 3)


def Ellipse():
    points = []
    t = 0
    while t <= pi * 2:
        points.append((2 * cos(t), 1.5 * sin(t)))
        t += 0.0001 * pi

    return convert_float_to_int(points, 3)


def Lissajous():
    points = []
    t = 0
    while t <= pi * 2:
        points.append(((sin(t * 3)), (sin(t * 4))))
        t += 0.0001 * pi

    return convert_float_to_int(points, 3)


def random_scatter():
    points = []
    for i in range(100):
        points.append((random.randint(-100, 100), random.randint(-100, 100)))

    return points


if __name__ == "__main__":
    scatter_plot_int(Astroid(), 10)
    scatter_plot_int(Cardioid(), 10)
    scatter_plot_int(Cycle(), 10)
    scatter_plot_int(Cycloid(), 10)
    scatter_plot_int(Ellipse(), 10)
    scatter_plot_int(Lissajous(), 10)
