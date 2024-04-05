import turtle
import sys
#defines etchasketh with custom user height and width
def etchasketch(width, height):
    width=int(width)
    height=int(height)
    #creates turtle screen size and play space
    turtle.speed(3)
    screen = turtle.Screen()
    screen.setup(width, height)

    move = False
    exit_flag = False
    #forces minimum screen size to 200x200, greater sizes are allowed
    if (width < 200):
        width=200
    if (height < 200):
        height=200
    #defines 'q' = close function
    def end_condition():
        turtle.bye()
        return True
    #defines 'p' will toggle pen up or down each press
    def pen_up():
        if (turtle.isdown()==True):
            turtle.up()
        elif(turtle.isdown()== False):
            turtle.down()
    #up function, will change move to true, rotate the turtle up, and move him .5 pixels per tick.
    #if statement tracks turtle and teleports when he hits the boarder
    def up():
        global move
        move = True
        turtle.setheading(90)
        while 0==0:
            if move:
                turtle.forward(0.5)
            screen.update()
            #print(turtle.ycor())
            if turtle.ycor() > (height/2):
                turtle.goto(turtle.xcor(), -((height/2)))
    def down():
        global move
        move = True
        turtle.setheading(270)
        while 0==0:
            if move:
                turtle.forward(0.5)
            screen.update()
            if turtle.ycor() < -(height/2):
                turtle.goto(turtle.xcor(), ((height/2)))
    def right():
        global move
        move = True
        turtle.setheading(0)
        while 0==0:
            if move:
                turtle.forward(0.5)
            screen.update()
            if turtle.xcor() > (width/2):
                turtle.goto(-((width/2)), turtle.ycor())
    def left():
        global move
        move = True
        turtle.setheading(180)
        while 0==0:
            if move:
                turtle.forward(0.5)
            screen.update()
            if turtle.xcor() < -(width/2):
                turtle.goto(((width/2)), turtle.ycor())
    #binds movement, pen up, and sentinal key, also tells turtle to listen for those keystrokes
    turtle.onkey(up, 'w')
    turtle.onkey(down, 's')
    turtle.onkey(right, 'd')
    turtle.onkey(left, 'a')
    turtle.onkey(pen_up, 'p')
    turtle.onkey(end_condition, 'q')
    turtle.listen()
#main function prompts user height and width, and runs etchasketch
def main():
    width=input("Enter screen width. ")
    height=input("Enter screen height. ")
    etchasketch(width, height)
main()

