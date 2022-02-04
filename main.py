import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.color("white")
t.speed(0)
t.width(6)
n = 200
shade = 0
bri = 0.4
for i in range (200):
    t.left(145)
    for c in range (1):
        t.forward(i*2)
        c = colorsys.hsv_to_rgb(shade,1,0.8)
        shade = shade + 0.01
        t.color(c)


turtle.exitonclick()