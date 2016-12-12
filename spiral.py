import webbrowser
import turtle

# ------------------
# Bring up sprial gif
# ------------------
new = 2 # open in a new tab, if possible
url = "file:///Users/maxfreundlich/Desktop/myillusion/spiral.gif"
webbrowser.open(url,new=new)

# ------------------
# Create window 
# ------------------
window = turtle.Screen()

# ------------------
# Draw RED sprial
# ------------------

redPen = turtle.Turtle()
redPen.speed(0)
redPen.color("#FF0000")

side=5
redPen.penup()
redPen.goto(0,0)
redPen.pendown()

for i in range (1,350):
  redPen.forward(side)
  redPen.left(62)
  side=side+1

redPen.penup()
redPen.goto(500,500)

# ------------------
# Draw BLUE sprial
# ------------------

bluePen = turtle.Turtle()
bluePen.speed(0)
bluePen.color("#0000FF")

side=5
bluePen.penup()
bluePen.goto(1,1) #offset
bluePen.pendown()

for i in range (1,350):
    bluePen.forward(side)
    bluePen.left(62)
    side=side+1

bluePen.penup()
bluePen.goto(500,500)

# ------------------
# Only close window on click
# ------------------
window.exitonclick()