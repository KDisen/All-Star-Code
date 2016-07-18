#Keven & Joshua
# Paint Shop
from Processing import *
window(400,400)
fill(255,0,0)
rect(0,0,200,50)
fill (0,255,0)
rect(200,0,200,50)
Red= fill(255,0,0)

def doMouseClicked():
    print('mouse clicked at' + str(mouseX()) + ', ' + str(mouseY()) )
    x=0
    if mouseX() >0 and mouseX() <200 and mouseY() >0 and mouseY() <200:
        stroke(255,0,0)
    elif mouseX() > 200 and mouseX() <400 and mouseY()>0 and mouseY()< 200:
        stroke(0,255,0)

onMouseClicked+= doMouseClicked



def doMouseDragged():
    if mouseY() >50:
        line(pmouseX(), pmouseY(), mouseX(), mouseY())
        
        
        
   
  
        
onMouseDragged += doMouseDragged




 