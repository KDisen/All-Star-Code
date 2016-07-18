from Myro import *
init("sim")
def Dance1():
    i=0
    while i<4:
        forward(2,1)
        backward(2,1)
        turnBy(90)
        i=i+1
def Dance2():
    i=0
    while i<2:
        turnRight(2,1)
        forward(2,1)
        turnLeft(2,1)
        forward(2,1))
        i=i+1