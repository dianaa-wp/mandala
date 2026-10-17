import turtle
import colorsys
import math

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("Hearts mandala")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


def hsv(h, s=1.0, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


def heart(cx, cy, size, angle):

    s = size / 16.0
    th = math.radians(angle)
    c, sn = math.cos(th), math.sin(th)
    first = True
    for k in range(0, 61):
        p = 2 * math.pi * k / 60
        x = 16 * math.sin(p) ** 3
        y = (13 * math.cos(p) - 5 * math.cos(2 * p)
             - 2 * math.cos(3 * p) - math.cos(4 * p)) + 2.5
        x, y = x * s, y * s
        px = cx + x * c - y * sn
        py = cy + x * sn + y * c
        if first:
            t.penup()
            t.goto(px, py)
            t.pendown()
            first = False
        else:
            t.goto(px, py)


def ring(n, R, size, hue0, width=1, hue_turns=1.0, spin=0, val=1.0):

    t.pensize(width)
    for i in range(n):
        a = 360.0 * i / n
        rad = math.radians(a)
        cx, cy = R * math.cos(rad), R * math.sin(rad)
        t.pencolor(hsv(hue0 + hue_turns * i / n, 1.0, val))
        heart(cx, cy, size, a - 90 + spin)
        if i % 3 == 0:
            screen.update()



ring(90, 300, 90, 0.00, width=1, hue_turns=1.0)
ring(72, 220, 75, 0.33, width=1, hue_turns=2.0, spin=15, val=0.95)
ring(54, 140, 60, 0.66, width=2, hue_turns=1.0, spin=-15)
ring(36, 70, 40, 0.15, width=2, hue_turns=3.0)

t.pensize(2)
for j in range(12):
    t.pencolor(hsv(0.9 + j / 24))
    heart(0, 0, 8 + j * 3, 0)
    screen.update()

screen.update()
turtle.done()