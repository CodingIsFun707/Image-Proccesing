from turtle import *
import turtle
import math

colormode(255)
pencolor("black")
hideturtle()
screensize(900,900)
tracer(False)

Grid = []

for i in range(1,901):
    Grid.append(255)

def Square(x1,y1,x2,y2,fill):
    fillcolor(fill,fill,fill)
    begin_fill()
    up()
    goto(x1,y1)
    down()
    setx(x2)
    sety(y2)
    setx(x1)
    sety(y1)
    end_fill()
    

def Draw():
    for i in range(0,30):
        for j in range(0,31):
            if ((30 * i) + j) < 900:
                Square((-450 + (30 * j)),(-450 + (30 * i)),(-420 + (30 * j)),(-420 + (30 * i)),Grid[(30 * i) + j])
    update()

def Fxn(x,y,):
    NewX = x + 450
    NewY = y + 450
    index = ((NewX - (NewX % 30)) / 30) + (NewY - (NewY % 30))
    Grid[int(index)] = 0
    Square((x - (x % 30)),(y - (y % 30)),(x - (x % 30) + 30),(y - (y % 30) + 30), Grid[int(index)])
    
def Blur():
    BlurGrid = []
    for i in range(0,900):
        AllDirs = [(i-31),(i-30),(i-29),(i-1),i,(i+1),(i+29),(i+30),(i+31)]
        AllDirsValue = []
        RunningSum = 0
        NumElements = 0
        SqrsX = 0
        SqrsY = 0
        NewX = 0
        NewY = 0
        global Grid
        for j in AllDirs:
            try:
                AllDirsValue.append(Grid[j])
            except:
                pass
        for j in AllDirsValue:
            RunningSum = RunningSum + j
            NumElements += 1
    
        BlurGrid.append(RunningSum//NumElements)
        SqrsX = (i - 1) % 30
        SqrsY = math.floor(i / 30)
        NewX = (SqrsX * 30) - 450
        NewY = (SqrsY * 30) - 450
        Square(NewX,NewY,(NewX + 30),(NewY +30),BlurGrid[(i-1)])

    Grid = BlurGrid

Draw()

wn = turtle.Screen()
wn.onclick(Fxn)
turtle.onkey(Blur,"k")
turtle.listen()
wn.mainloop()
