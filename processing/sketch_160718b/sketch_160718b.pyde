def setup():
    size(500,500)
value = 0
def draw():
    fill (value)
    background(255)
    ellipse(mouseX, 50, mouseX, 80)
    fill(255,0,0)
    rect(mouseY, 100, mouseY, 90)
    ellipse(mouseX, 400, mouseY, 100)
    line(mouseX,250,mouseY,95)
    fill(200,150,90)
def mouseMoved():
    global value
    value=value+5
    if value> 255:
        value=0