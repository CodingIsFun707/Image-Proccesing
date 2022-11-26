from turtle import *
import turtle
import math

ScreenSize = 900
Cellsize = 23

colormode(255)
pencolor("black")
hideturtle()
screensize(ScreenSize,ScreenSize)
tracer(False)

Grid = []

NumRowsColumns = int(ScreenSize / Cellsize)
TotalCells = int(NumRowsColumns * NumRowsColumns)

for i in range(0,TotalCells):
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
    for i in range(0,NumRowsColumns):
        for j in range(0,(NumRowsColumns + 1)):
            if ((NumRowsColumns * i) + j) < TotalCells:
                Square(((0 - (ScreenSize / 2)) + (Cellsize * j)),((0 - (ScreenSize / 2)) + (Cellsize * i)),((0 - (ScreenSize / 2)) + (Cellsize * j) + Cellsize),((0 - (ScreenSize / 2)) + (Cellsize * i) + Cellsize),Grid[(Cellsize * i) + j])
    update()

def Fxn(x,y,):
    NewX = x + (ScreenSize / 2)
    NewY = y + (ScreenSize / 2)
    index = ((NewX - (NewX % Cellsize)) / Cellsize) + (NewY - (NewY % Cellsize))
    Grid[int(index)] = 0
    BottomCX = x - (x % Cellsize)
    BottomCY = y - (y % Cellsize)
    Square(BottomCX,BottomCY,(BottomCX + Cellsize),(BottomCY + Cellsize), Grid[int(index)])
    #Square((x - (x % Cellsize)),(y - (y % Cellsize)),(x - (x % Cellsize) + Cellsize),(y - (y % Cellsize) + Cellsize), Grid[int(index)])
    
def Blur():
    BlurGrid = []
    for i in range(0,TotalCells):
        AllDirs = [(i - (NumRowsColumns + 1)),(i - (NumRowsColumns)),(i - (NumRowsColumns - 1)),(i - 1),i,(i + 1),(i + (NumRowsColumns - 1)),(i + (NumRowsColumns)),(i + (NumRowsColumns + 1))]
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
        SqrsX = (i - 1) % NumRowsColumns
        SqrsY = math.floor(i / NumRowsColumns)
        NewX = (SqrsX * Cellsize) - (ScreenSize / 2)
        NewY = (SqrsY * Cellsize) - (ScreenSize / 2)
        Square(NewX,NewY,(NewX + Cellsize),(NewY + Cellsize),BlurGrid[(i-1)])

    Grid = BlurGrid

Draw()

wn = turtle.Screen()
wn.onclick(Fxn)
#turtle.onkey(Blur,"k")
#turtle.listen()
wn.mainloop()
