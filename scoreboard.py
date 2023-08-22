from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(None)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.score = 0
   
    def show_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def replay(self):
        return screen.textinput(title="Play again?", prompt="Would you like to play again? 'y' or 'n': ")
        