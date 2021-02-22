from tkinter.constants import CENTER
from turtle import *
from time import *

time_start = perf_counter()
print(time_start)


wn = Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)

Players = ['Player A', 'Player B']

game_over = Turtle()
game_over.speed(5)
game_over.color("white")
game_over.hideturtle()
game_over.penup()
game_over.goto(0, 0)


pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

border = Turtle()
border.penup()
border.color("white")
border.setx(380)
border.right(90)
border.pendown()
border.fd(280)
border.right(90)
border.fd(770)
border.right(90)
border.fd(520)
border.rt(90)
border.fd(390)
border.rt(90)
border.fd(520)
border.bk(520)
border.lt(90)
border.fd(380)
border.rt(90)
border.fd(280)
border.hideturtle()


paddle_a = Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
# ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5


def paddle_a_up():
    y = paddle_a.ycor()
    if y <= 170:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -210:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y <= 170:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y >= -210:
        y -= 20
    paddle_b.sety(y)


Score_a = 0
Score_b = 0

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

pen.write(f"{Players[0]}: {Score_a} {Players[1]}: {Score_b}",
          align=CENTER, font=("Courier", 24, "normal"))


num_a = 4
num_b = 4
Lives_a = [Turtle(), Turtle(), Turtle(), Turtle()]
Lives_b = [Turtle(), Turtle(), Turtle(), Turtle()]


def Life_a(n):

    for i in Lives_a:
        i.hideturtle()
    for j, i in enumerate(Lives_a[:n]):
        i.showturtle()
        i.color("white")
        i.shape("square")
        i.shapesize(2, 1)
        i.penup()
        i.goto(270 + (30*j), 270)


def Life_b(n):
    for i in Lives_b:
        i.hideturtle()
    for j, i in enumerate(Lives_b[:n]):
        i.showturtle()
        i.color("white")
        i.shape("square")
        i.shapesize(2, 1)
        i.penup()
        i.goto(-(270 + (30*j)), 270)


def GameOver(n):
    ball.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()
    game_over.write(f'  GAME OVER\n{Players[n]} WINS', align=CENTER, font=(
        "Courier", 36, "bold"))
    border.clear()


# Main Game Loop
while True:
    wn.update()
    time_end = perf_counter()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    Life_a(num_a)
    Life_b(num_b)

    if ball.ycor() > 230:
        ball.sety(230)
        ball.dy *= -1
    if ball.ycor() < -270:
        ball.sety(-270)
        ball.dy *= -1

    if (ball.xcor() > 370):
        ball.goto(0, 0)
        time_start = time_end
        if ball.dx < 0:
            ball.dx = -0.5
        else:
            ball.dx = 0.5
        if ball.dy < 0:
            ball.dy = -0.5
        else:
            ball.dy = 0.5
        ball.dx *= -1
        num_a -= 1

    if ball.xcor() < -380:
        ball.goto(0, 0)
        time_start = time_end
        if ball.dx < 0:
            ball.dx = -0.5
        else:
            ball.dx = 0.5
        if ball.dy < 0:
            ball.dy = -0.5
        else:
            ball.dy = 0.5
        ball.dx *= -1
        num_b -= 1

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
        ball.setx(340)
        Score_b += 1
        pen.clear()
        pen.write(f"Player A: {Score_a} Player B: {Score_b}",
                  align=CENTER, font=("Courier", 24, "normal"))

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1
        ball.setx(-340)
        Score_a += 1
        pen.clear()
        pen.write(f"Player A: {Score_a} Player B: {Score_b}",
                  align=CENTER, font=("Courier", 24, "normal"))

    if (num_a == 0):
        GameOver(0)

    if(num_b == 0):
        GameOver(1)

    if time_end - time_start >= 15:
        ball.dx *= 1.25
        ball.dy *= 1.25
        time_start = time_end
