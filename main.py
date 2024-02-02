import datetime
import random

from PIL import Image, ImageDraw

BLUE = (68, 114, 196)
GRAY = (128, 128, 128)
SCALE = 10
MARGIN = 0

timestamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H%M%S")


def scatter_plot_int(input):
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

    image = image.resize((width * SCALE, height * SCALE), Image.NEAREST)
    image.save(f"./outputs/result_{timestamp}.png")
    # image.show()


if __name__ == "__main__":
    input = []
    for i in range(100):
        input.append((random.randint(-100, 100), random.randint(-100, 100)))

    scatter_plot_int(input)
