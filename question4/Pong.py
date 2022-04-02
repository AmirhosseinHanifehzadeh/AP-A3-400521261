from tkinter import * 
from tkinter import messagebox
import time


# building a window
root = Tk()

#adding window title
root.title("AP4002 Pong Game")
root.resizable(False, False)
canvas = Canvas(root, width=500, height=400, bg='turquoise')
canvas.grid(row=0,column=0)

class Ball:
    def __init__(self, canvas,bgColor, size, paddle):
        self.canvas = canvas
        self.paddle = paddle 
        self.circle = canvas.create_oval(30,30, size, size, fill=bgColor) # create ball 
        self.canvas.move(self.circle, 245, 100)
        self.mode = 1 # ball's moving speed 
        self.deltax = self.mode
        self.deltay = self.mode 
        self.hitbottom = False
        self.score = 0

    def move(self):
        self.canvas.move(self.circle, self.deltax, self.deltay)
        ball_pos = canvas.coords(self.circle) 

        if ball_pos[0] <= 0:
            self.deltax = self.mode
        if ball_pos[2] >= 500:
            self.deltax = self.mode * -1
        if ball_pos[1] <= 0:
            self.deltay = self.mode 
        if ball_pos[3] >= 400:
            self.hitbottom = True
        if self.hitPaddle(ball_pos):
            self.deltay = self.mode * -1
            self.score += 1 * self.mode 
    
    def hitPaddle(self, ball_pos):
        """check that if ball hit the paddle"""
        paddle_pos = self.canvas.coords(self.paddle.rect)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                return True

class Paddle:
    def __init__(self, canvas, bgColor):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(0,0, 100, 10, fill=bgColor)
        self.deltax = 0 
        self.mode = 1 # paddle's moving speed 
        self.canvas.move(self.rect, 200, 300)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)

    def draw(self):
        self.canvas.move(self.rect, self.deltax, 0)
        pos = self.canvas.coords(self.rect)

        if pos[0] <= 0:
            # preventing going out of frame
            self.deltax = 0

        if pos[2] >= 500:
            # preventing going out of frame
            self.deltax = 0 

    def move_left(self, event):
        """function to moving paddle to left"""
        self.deltax = -2 * self.mode 
    def move_right(self, event):
        """function to moving paddle to right"""
        self.deltax = 2 * self.mode 

# instantiating 
paddle = Paddle(canvas, 'red')
ball = Ball(canvas, 'red', 50, paddle)

while ball.hitbottom == False:
    ball.move()
    paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.001)

# Game Over
messagebox.showinfo(title = "GAVE OVER", message = "YOU LOST")
root.update()