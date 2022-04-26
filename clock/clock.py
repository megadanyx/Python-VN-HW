import turtle as t
# time data

c_radius = 200

# ptint to screen date!
# shows on the screen

def printTime(hours ,minutes ,seconds):
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

def DrowClock(hours ,minutes ,seconds):
    t.clear()
    DrawClockCircle()
    DrowClockHours(hours)
    DrowClockMinutes(minutes)
    DrowClockSecunds(seconds)

def DrawClockCircle():
    t.speed(0)
    t.color("green")
    t.pensize(3)
    t.penup()
    t.setheading(0)
    t.setposition(0,-c_radius)
    t.pendown()
    t.circle(c_radius)
def DrowClockHours(hours):
    t.penup()
    t.setposition(0,0)
    t.setheading(90 + hours * -30)
    t.pendown()
    t.color("black")
    t.pensize(4)
    t.forward(c_radius * 0.70)
 
def DrowClockMinutes(minutes):
    t.penup()
    t.setposition(0,0)
    t.setheading(90 + minutes * -6)
    t.pendown()
    t.color("black")
    t.pensize(2)
    t.forward(c_radius * 0.80)
 
def DrowClockSecunds(secunds):
    t.penup()
    t.setposition(0,0)
    t.setheading(90 + secunds * -6)
    t.pendown()
    t.color("black")
    t.pensize(1)
    t.forward(c_radius * 0.85)
