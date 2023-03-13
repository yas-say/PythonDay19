from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "green", "yellow", "blue", "purple"]


screen = Screen()

screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Enter your bet...", prompt="Which color turtle will win?")
print(user_bet)

tim=[]
print(screen.window_height())
xcord = -230
ycord = ((screen.window_height()/2)-30)* -1

for _ in colors:
    myturtle = Turtle(shape="turtle")
    myturtle.color(_)
    myturtle.penup()
    tim.append(myturtle)
    myturtle.goto(x=-230, y= ycord)
    ycord+= (screen.window_height()/len(colors))
winner=""
flag = True
while flag:
    for _ in tim:
        _.forward(randint(0,10))
        if _.xcor() >= 250:
            flag = False
            winner = _.color()
            break

print(f"Winner is {winner}")


screen.exitonclick()
