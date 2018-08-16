import turtle
import random
import time
screen = turtle.Screen()
screen.setup(1000,1000)
screen.bgpic("background.gif")
player = turtle
score=0
score1=turtle.Turtle()
score1.hideturtle()
score1.penup()
score1.goto(0,-500)
xpos = [-240, -160, -80, 0, 80, 160, 240]
random_xpos = random.choice(xpos)
#creating borders
title = turtle.Turtle()
title.penup()
title.goto(0,400)
title.write("Dunkin' Trash", font=("Comic Sans MS",60),align="center")
title.hideturtle()
border = turtle.Turtle()
border.speed(0)
border.penup()
border.goto(-400,-400)
border.pendown()
border.goto(-400,400)
border.goto(400,400)
border.goto(400,-400)
border.goto(-400,-400)
border.hideturtle()


#making the player move
def player_move():

    def right():
        if player.xcor() > 280:
            player.setpos(280,-300)
        else:
            player.forward(80)

    def left():
        if player.xcor() < -280:
            player.setpos(-280,-300)
        else:
           player.back(80)

    turtle.onkeypress(right, "Right")

    turtle.onkeypress(left, "Left")

    turtle.listen()

#creating the recycle bin


player.penup()
turtle.register_shape("recyclebin.gif")
player.shape("recyclebin.gif")
player.goto(0,-300)

#falling trash function

def falling_trash():
    turtle.register_shape("bottle.gif")
    global score, random_xpos
    random_xpos = random.choice(xpos)
    trash = turtle.Turtle()
    trash.shape("bottle.gif")
    trash.hideturtle()
    trash.speed(0)
    trash.setheading(270)
    trash.penup()
    trash.setpos(random_xpos,400)
    trash.showturtle()
    falling_speed = 5
    if score > 10:
        falling_speed = 7
    if score > 20:
        falling_speed = 9
    if score > 30:
        falling_speed = 11
    while trash.pos()[1] > -270:
        player_move()
        trash.forward(falling_speed)
    if abs(trash.pos()[0] - player.pos()[0]) < 1:
        score +=1
        score1.clear()
        score1.write(score, font=("Comic Sans MS",60),align=("center"))

        
        
    else:
        score1.goto(0,0)
        score1.color("red")
        score1.write("GAME OVER", font = ("Comic Sans MS", 100), align = ("center"))
        time.sleep(2)
        quit()
     
        
    trash.hideturtle()
        

while True:
    
    falling_trash()
   

    

turtle.listen()
turtle.mainloop()



