import turtle


def koch_dlugie(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)
        t.right(120)
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


t = turtle.Turtle()
wn = turtle.Screen()
koch_dlugie(t, 3, 200)
t.right(120)
koch(t, 3, 200)
t.right(120)
koch(t, 3, 200)
wn.exitonclick()
