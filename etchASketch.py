from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def w_move_forward():
    tim.forward(10)


def s_move_backward():
    tim.backward(10)


def a_counter_clockwise():
    tim.left(10)
    tim.forward(10)


def d_clockwise():
    tim.right(10)
    tim.forward(10)


def c_clear():
    tim.reset()


screen.listen()

screen.onkey(key="w", fun=w_move_forward)
screen.onkey(key="s", fun=s_move_backward)
screen.onkey(key="a", fun=a_counter_clockwise)
screen.onkey(key="d", fun=d_clockwise)
screen.onkey(key="c", fun=c_clear)

screen.exitonclick()
