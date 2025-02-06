import turtle
import random
#screen oluşturma
game_board = turtle.Screen()
game_board.bgcolor("pink")
game_board.title("Catch the Turtle")
screen_width = game_board.window_width() // 2
screen_height = game_board.window_height() // 2

#turtle yaratmak
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(1.5)
my_turtle.color("green")

#time
timer=turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 210)
game_time=60
def countdown():
    global game_time
    timer.clear()
    if game_time > 0:
        timer.write(f"Time Left: {game_time} sec", align="center", font=("Arial", 20, "bold"))
        game_time -= 1
        game_board.ontimer(countdown, 1000)
        move_turtle()
    else:
        timer.write("Game Over!", align="center", font=("Arial", 20, "bold"))


#click anlama
click_turtle = turtle.Turtle()
click_turtle.hideturtle()
click_turtle.penup()
clicked_position = (0, 0)

#skor sayma
skor_turtle=turtle.Turtle()
skor_turtle.hideturtle()
skor_turtle.penup()
skor_turtle.goto(0, 180)
skor=0
#skor yazdırma fonksiyonu
def update():
    skor_turtle.clear()
    skor_turtle.write(f"Skor: {skor} point", align="center", font=("Arial", 20, "bold"))

#catch/click olunca skor artacak
def click(x, y):
    global skor
    update()
    if game_time > 0:
        if abs(x - random_width) < 30 and abs(y - random_height) < 30:
            skor += 1
            update()

#turtle move random olsun
def move_turtle():
    my_turtle.speed(2)
    my_turtle.penup()
    global random_width, random_height
    random_width = random.randint(-screen_width, screen_width)
    random_height = random.randint(-screen_height, screen_height-120)
    my_turtle.setpos(random_width, random_height)

def start_game():
    countdown()
    update()

game_board.onclick(click)
move_turtle()
start_game()
game_board.mainloop()