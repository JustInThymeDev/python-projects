from turtle import *
from Lab2_functions import *
MORTAR = 2
def main():
    setworldcoordinates(0,400,650,0)
    clear()
    shape('turtle')
    pencolor('olive drab')
    fillcolor('sienna')
    bgcolor('grey')
    x=0
    y=0
    width=20
    height=20
    offset=0
    for i in range(0, 4):
        draw_rect(x, y, width, height, "Black")
        draw_line(x, y, x+width, y+width, "Blue")
        draw_line(x+width, y, x, y+width, "Blue")
        draw_rect(x+width, y, width, height, "White")
        x=x+(width*2)
    x=50
    y=70
    width=30
    height=30
    for i in range(0, 5):
        draw_rect(x, y, width, height, "Black")
        draw_line(x, y, x+width, y+width, "Blue")
        draw_line(x+width, y, x, y+width, "Blue")
        draw_rect(x+width, y, width, height, "White")
        x=x+(width*2)
    x=10
    y=150
    width=25
    height=25
    for j in range(0, 8):
        y=y+height+MORTAR
        x=10
        for i in range(0, 4):
            draw_rect(x, y, width, height, "Black")
            draw_line(x, y, x+width, y+width, "Blue")
            draw_line(x+width, y, x, y+width, "Blue")
            draw_rect(x+width, y, width, height, "White")
            x=x+(width*2)
    x=400
    y=0
    width=35
    height=35
    offset=35
    for j in range(0, 4):
        y=y+height+MORTAR
        if j%2==1:
            x=400+offset
        else:
            x=400
        for i in range(0, 2):
            draw_rect(x, y, width, height, "Black")
            draw_line(x, y, x+width, y+width, "Blue")
            draw_line(x+width, y, x, y+width, "Blue")
            draw_rect(x+width, y, width, height, "White")
            x=x+(width*2)
    x=250
    y=200
    width=25
    height=25
    offset=10
    for j in range(0, 6):
        y=y+height+MORTAR
        if j%2==1:
            x=250+offset
        else:
            x=250
        for i in range(0, 3):
            draw_rect(x, y, width, height, "Black")
            draw_line(x, y, x+width, y+width, "Blue")
            draw_line(x+width, y, x, y+width, "Blue")
            draw_rect(x+width, y, width, height, "White")
            x=x+(width*2)
    x=425
    y=180
    width=20
    height=20
    offset=10
    for j in range(0, 10):
        y=y+height+MORTAR
        if j%2==1:
            x=425+offset
        else:
            x=425
        for i in range(0, 5):
            draw_rect(x, y, width, height, "Black")
            draw_line(x, y, x+width, y+width, "Blue")
            draw_line(x+width, y, x, y+width, "Blue")
            draw_rect(x+width, y, width, height, "White")
            x=x+(width*2)



main()


