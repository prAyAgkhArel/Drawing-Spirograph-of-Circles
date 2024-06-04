import turtle as t
import random

timmy = t.Turtle()

t.colormode(255)
timmy.pensize(2)
timmy.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

angle = 5
for _ in range(int(360/angle)):
    timmy.color(random_color())
    timmy.circle(80)       #draws circle of radius 80
    current_heading = timmy.heading()        # heading() return float to which dirn it is heading
    timmy.setheading(current_heading + angle) #setheading() allows us to set head of turtle arrow








screen = t.Screen()
screen.exitonclick()


