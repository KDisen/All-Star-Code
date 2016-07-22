from Processing import *
window(700,700)
fill(0,0,0)
background(255,255,255)
x=25
yChange=25
badShipY=100     
ellipseX = x
i=0    
rect(x,600,150,25)
def ship():
    fill(255,255,255)
    rect(25,600,150,25)
ship()

def draw():
    background(0,0,0)
    rect(x,600,150,25)
    delay(1)

def doKeyPressed():
    global x,y, ellipseY
    if key() == 'Left':
        if x>0:
            x=x-5
            draw()
                
    if key() == 'Right':
        if x<550:
            x=x+5
            draw()
     
    if key()=='a':
        while ellipseY > 10:
            shoot()
            delay(10)

        
    
onKeyPressed += doKeyPressed

onKeyPressed += doKeyPressed
    
def shoot():
    global x,y,ellipseX
    y=600
    fill(255,255,255)
    x=ellipseX
    ellipse(ellipseX,y,10,10)
    
    
    while y >= 0:
        y=y-1
        fill(255,255,255)
        ellipse(ellipseX,y,10,10)
        
        
        delay(1)
        
    
    y=600
    rect(x,y,150,20)
    ellipseY = y

def badShips():
    global badShipY,yChange,newY,i
    while i<24:
        #newY=badShipY+yChange*i
        background(0,0,0)
        draw()
        global y
        doKeyPressed()
        fill(255,255,255)
        rect(50,100,25,25)
        rect(100,100,25,25)
        rect(150,100,25,25)
        rect(200,100,25,25)
       
        if ellipseX==50 and ellipseY==100:
            fill(0,0,0)
            rect(50,100,25,25)
        fill(255,255,255)
        rect(100,100,25,25)
        if ellipseX==100 and ellipseY==100:
            fill(0,0,0)
            rect(50,100,25,25)
        fill(255,255,255)
        rect(150,100,25,25)
        if ellipseX==150 and ellipseY==100:
            fill(0,0,0)
            rect(50,100,25,25)
        fill(255,255,255)
        rect(200,100,25,25)
        if ellipseX==200 and ellipseY==100:
            fill(0,0,0)
            rect(50,100,25,25)
        delay(1500)
        i=i+1
badShips()      

  