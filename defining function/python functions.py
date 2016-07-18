from Myro import *
init("sim")
penDown()
length=3
def square(length):
    i=0
    while i<4:
        turnBy(90)
        forward(1,length)
        i=i+1
square(4)