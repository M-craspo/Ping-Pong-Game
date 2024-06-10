import turtle

# Create the main window class
class GameWindow:
    def __init__(self):
        self.wind = turtle.Screen()
        self.wind.title("PING PONG")
        self.wind.bgcolor("white")
        self.wind.setup(width=800, height=600)
        self.wind.tracer(0) #for stop updating automatically

    def update(self):
        self.wind.update()

# Create the Paddle class
class Paddle:
    def __init__(self, x, y, color):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def go_up(self):
        y = self.paddle.ycor()
        if y < 250:  # Prevent paddle from going out of the window
            y += 20
        self.paddle.sety(y)

    def go_down(self):
        y = self.paddle.ycor()
        if y > -240:  # Prevent paddle from going out of the window
            y -= 20
        self.paddle.sety(y)

# Create the Ball class
class Ball:
    def __init__(self, color):
        self.ball = turtle.Turtle()
        self.ball.speed(10)
        self.ball.shape("circle")  # Change shape to circle
        self.ball.color(color)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        # Border checking
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            return "left"

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            return "right"
        return None

# Create the Scoreboard class
class Scoreboard:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Player 1: {self.score1}  Player 2: {self.score2}", align="center", font=("Courier", 24, "normal"))

    def increase_score1(self):
        self.score1 += 1
        self.update_score()

    def increase_score2(self):
        self.score2 += 1
        self.update_score()

def main():
    game_window = GameWindow()

    # Create paddles
    paddle1 = Paddle(-350, 0, "blue")
    paddle2 = Paddle(350, 0, "red")

    # Create ball
    ball = Ball("black")

    # Create scoreboard
    scoreboard = Scoreboard()

    # Keyboard bindings
    game_window.wind.listen()
    game_window.wind.onkeypress(paddle1.go_up, "w")
    game_window.wind.onkeypress(paddle1.go_down, "s")
    game_window.wind.onkeypress(paddle2.go_up, "Up")
    game_window.wind.onkeypress(paddle2.go_down, "Down")

    # Main game loop
    while True:
        game_window.update()
        scorer = ball.move()

        # Update score
        if scorer == "left":
            scoreboard.increase_score2()
        elif scorer == "right":
            scoreboard.increase_score1()

        # Paddle and ball collisions
        if (ball.ball.dx > 0) and (350 > ball.ball.xcor() > 340) and (paddle2.paddle.ycor() + 50 > ball.ball.ycor() > paddle2.paddle.ycor() - 50):
            ball.ball.setx(340)
            ball.ball.dx *= -1

        if (ball.ball.dx < 0) and (-350 < ball.ball.xcor() < -340) and (paddle1.paddle.ycor() + 50 > ball.ball.ycor() > paddle1.paddle.ycor() - 50):
            ball.ball.setx(-340)
            ball.ball.dx *= -1

if __name__ == "__main__":
    main()
