from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet (red, orange, yellow, green, blue, purple)", prompt="Which turtle will win the race? Enter a color: ").lower().strip()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -150
for turtle_index in range(6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.speed(2)
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.goto(x=-240, y=y)
	all_turtles.append(new_turtle)
	y += 50

if user_bet:
	is_race_on = True

winner = "green"

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 230:
			winner = turtle.pencolor()
			is_race_on = False
		random_distance = randint(0, 10)
		turtle.forward(random_distance)

if winner == user_bet:
	print(f"You won! The {winner} turtle is the winner!")
else:
	print(f"You lost! The {winner} turtle is the winner!")

screen.exitonclick()
