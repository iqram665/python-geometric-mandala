import turtle

# screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Turtle Geometric Design by Iqram")

# title setup
t = turtle.Turtle()
t.speed(0) # Maximum speed
t.width(2)

# Color list (vibrant shades like the video)
colors = ["#CE5FBB", "#44B69D", "#DAF7A6", "#C70039", "#900C3F"]

# Geometric pattern drawing logic
for i in range(300):
    t.pencolor(colors[i % 5])
    t.forward(i * 1.8) # Increase the distance for a more expansive design
    t.left(145) # This angle will create the spiky look like in your video

# Add text (in the style of your video)
t.penup()
t.goto(0, -250)
t.pencolor("white")
t.write("Iqram geometric mandala design", align="center", font=("Arial", 16, "bold"))

t.hideturtle()
screen.exitonclick()