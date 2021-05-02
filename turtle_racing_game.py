from turtle import Turtle, Screen
import random


race = False
screen = Screen()
screen.title("Welcome to the turtle race!")
screen.setup(width=500, height=400)
screen.bgcolor("gray")
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a rainbow color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


y_axis = -70
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y_axis)
    y_axis += 30
    turtles.append(turtle)


if user_bet:
    race = True


while race:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winning_turtle = turtle.pencolor()
            screen.clear()
            turtle.color("black")
            turtle.goto(0, 0)
            if user_bet == winning_turtle:
                screen.bgcolor("green")
                turtle.write(f"You won!. The {winning_turtle} turtle is the winning turtle\n"
                             f"        Please click on the screen to exit", align="center", font=("Arial", 20, "normal"))
            else:
                screen.bgcolor("red")
                turtle.write(f"You lost. The {winning_turtle} turtle is the winning turtle\n"
                             f"        Please click on the screen to exit", align="center", font=("Arial", 20, "normal"))
        random_value = random.randint(1, 10)
        turtle.forward(random_value)

screen.exitonclick()

