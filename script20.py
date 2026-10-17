import turtle
import colorsys
import math

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("Mandala")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


def hsv(h, s=1.0, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


def ring(n, R, r, hue0, width=1, hue_turns=1.0, val=1.0):

    t.pensize(width)
    for i in range(n):
        a = 2 * math.pi * i / n
        cx, cy = R * math.cos(a), R * math.sin(a)
        t.pencolor(hsv(hue0 + hue_turns * i / n, 1.0, val))
        t.penup()
        t.goto(cx, cy - r)
        t.setheading(0)
        t.pendown()
        t.circle(r)
        if i % 3 == 0:
            screen.update()


def star(n, radius, hue0, width=1):

    t.pensize(width)
    pts = [(radius * math.cos(2 * math.pi * k / n),
            radius * math.sin(2 * math.pi * k / n)) for k in range(n)]
    step = n // 2 - 1 if (n // 2 - 1) > 1 else 2
    for k in range(n):
        x, y = pts[k]
        x2, y2 = pts[(k + step) % n]
        t.pencolor(hsv(hue0 + k / n))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x2, y2)
    screen.update()



ring(120, 190, 190, 0.00, width=1, hue_turns=1.0)
ring(80, 250, 120, 0.33, width=1, hue_turns=2.0, val=0.9)
ring(60, 120, 120, 0.66, width=2, hue_turns=1.0)
ring(36, 70, 70, 0.15, width=2, hue_turns=3.0)
star(72, 330, 0.5, width=1)

screen.update()
turtle.done()
