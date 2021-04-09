from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score = Score()

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)

# def go_up():
#     new_y = paddle.ycor() +20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     if paddle.ycor()>-260:
#         new_y = paddle.ycor() - 20
#         paddle.goto(paddle.xcor(), new_y)
#     else :
#         paddle.goto(paddle.xcor(), paddle.ycor())


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down , "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down , "s")

game_is_on =True
game_count=0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() >380  :
        ball.reset_position()
        score.l_point()
        game_count+=1

    if  ball.xcor() < -380 :
        ball.reset_position()
        score.r_point()
        game_count+=1


    if game_count == 3:
        game_is_on = False


# score.color("white")
# score.write(f"Game Over", align='center', font=('Arial', 30, 'normal'))


screen.exitonclick()