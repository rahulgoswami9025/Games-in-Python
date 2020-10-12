
'''
Building a Pong game

'''
import turtle

wn = turtle.Screen()                                        # Creating a window
wn.title('Pong by Rahul Goswami')
wn.bgcolor('black')                                         # Setting the window background colour
wn.setup(width = 800, height = 600)                         # Window dimensions
wn.tracer(0)                                                # to speed up the animations else too slow

# Creating Paddle A (left)

paddle_a = turtle.Turtle()                                  # Creating paddle with Turtle module : 
paddle_a.speed(0)                                           # max animation speed
paddle_a.shape('square')                                    # default square shape is 20px * 20px
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)          # Setting the size of the square
paddle_a.color('white')
paddle_a.penup()                                            # Turtle module draws a line when it moves by default and thus this penup() disable that line tracing.
paddle_a.goto(-350, 0)                                      # paddle starting postion ; -340 = left most pos , 0 = vertically centered

# Creating Paddle B (right)

paddle_b = turtle.Turtle()                                  # Creating paddle with Turtle module : 
paddle_b.speed(0)                                           # max animation speed
paddle_b.shape('square')                                    # default square shape is 20px * 20px
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)          # Setting the size of the square
paddle_b.color('white')
paddle_b.penup()                                            # Turtle module draws a line when it moves by default and thus this penup() disable that line tracing.
paddle_b.goto(350, 0)                                       # paddle starting postion ; -340 = left most pos , 0 = vertically centered

# Creating ball :

ball = turtle.Turtle()                                  
ball.speed(0)                                           
ball.shape('circle')                                            
ball.color('white')
ball.penup()                                            
ball.goto(0, 0)  

# Ball movements : 

ball.dx = 0.1                                                 # every time the ball moves by 0.1 px
ball.dy = -0.1


# Scoring mechanism : 

# Pen : 
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('PlayerA: 0  PlayerB: 0', align = 'center', font = ('Courier', 24, 'normal'))

# Score :
score_a = 0
score_b = 0




# Function to move paddles with keyboard inputs : 

# Func paddle A Up : (to move the paddle we need to know the current y_cordinate of the paddle)
# Note : y increase as we go up and decreases as we go down.

def paddle_a_up():
    y = paddle_a.ycor()                                     # y.cor() returns the y cordinate 
    y += 20                                                 # adds 20px to y co_ordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()                                     # y.cor() returns the y cordinate 
    y -= 20                                                 # adds 20px to y co_ordinate
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()                                     # y.cor() returns the y cordinate 
    y += 20                                                 # adds 20px to y co_ordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()                                     # y.cor() returns the y cordinate 
    y -= 20                                                 # adds 20px to y co_ordinate
    paddle_b.sety(y)
# keyboard binding : 

wn.listen()                                                 # this tell to listen for keyboard input
wn.onkeypress(paddle_a_up, 'w')                             # setting which keys will move paddle up 
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')                            
wn.onkeypress(paddle_b_down, 'Down')






# Main game loop : 

while True:
    wn.update()

    # move the ball 
    ball.setx(ball.xcor() + ball.dx)                        # ball move 0.1px every time
    ball.sety(ball.ycor() + ball.dy)
    

    # border setting (top and bottom) : 
    if ball.ycor() > 290:                                   # top co ordinate is 300 px from centre and ball size = 20 * 20 i.e radius = 10 px; thus 290
        ball.sety(290)
        ball.dy *= -1                                       # to stop ball from going offscreen

    if ball.ycor() < -290:                                  
        ball.sety(-290)
        ball.dy *= -1
    
    # right and left border : 

    if ball.xcor() > 390:
        ball.goto(0,0)                                      # to go back to center and move in reverse direction.
        ball.dx *= -1                                       # to stop ball from going offscreen on right side
        score_a += 1
        pen.clear()
        pen.write('PlayerA: {}  PlayerB: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24, 'normal'))

    
    if ball.xcor() < -390:
        ball.goto(0,0)                                      # to go back to center and move in reverse direction.
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('PlayerA: {}  PlayerB: {}'.format(score_a, score_b), align = 'center', font = ('Courier', 24, 'normal'))
        


    # paddle and ball collusion : 
    # paddle b collusion :

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    