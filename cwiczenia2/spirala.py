import turtle


def draw_spiral(my_turtle, line_len):
    if line_len < 106:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len + 5)


t = turtle.Turtle()
my_win = turtle.Screen()
draw_spiral(t, 10)
my_win.exitonclick()
