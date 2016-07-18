from Processing import *
window(400,400)
x=0
def draw():
    fill(x)
    rect(25,25,50,50)
def mouseMoved():
    global x
    x=x+5
    if x>225:
        x=0
    
