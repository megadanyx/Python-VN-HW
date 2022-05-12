######

import turtle as t
name = 'image/coin-1.gif'

# window setup
def WindowSetup():
    WIDTH  = 1300
    HEIGHT = 350
    t.setup(WIDTH, HEIGHT)
    t.showturtle()


#display any image 
def ShowImage(name):
    s = t.Screen()
    s.addshape(name)
    t.shape(name)

def ShowMarrio(x,y):
    name = 'image/marion-r-1.gif'
    s = t.Screen()
    s.addshape(name)
    t.setposition(x,y)
    t.shape(name)




