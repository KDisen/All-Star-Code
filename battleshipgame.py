#Keven and Nathan
#July 20, 2016
#BattleShip game
from Processing import *
from random import *
gameOver=False
def battleship():
    global gameOver
    window(400,400)
    grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    row= randrange(0,5)         #random range so the ship can change everytime you play
    column = randrange(0,5)
    grid[row][column] = 1
    width= 80
    height=80
    
    i=0 
    while i<5:
        newX= width*i
        line(newX,0,newX,400)       #Makes the lines of the x axis for grid
        i=i+1
    i=0
    while i<5:
        newY=height*i
        line(0,newY,400,newY)       #Makes lines of the y axis for grid
        i=i+1
        
        
    while gameOver==False:  
        row = int(input("which row"))           #input is your guess
        column= int(input("which column"))  
        if (grid[row][column]==1)== False:          #If you dont hit the ship then the place you chose will turn red
            print ("you missed")
            fill(255,0,0)
            rect(width*row,height*column,80,80)
        else:
            gameOver=True                         #If ship is hit it turns green and Game Over
            fill(0,255,0)
            rect(width*row,height*column,80,80)
            print("you hit")
battleship()        #Calling the function
        
        

    
    