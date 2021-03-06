from tkinter import *

from tkinter import font





class Info(Frame):

    def __init__(self, master=None):

        Frame.__init__(self)

        connect4 = font.Font(self, size=44, family='Arial')

        self.t = Label(self, text="CONNECT FOUR", font=connect4)

        self.t.grid()





class Point(object):

    def __init__(self, x, y, canvas, color="white"):

        self.canvas = canvas

        self.x = x

        self.y = y

        self.color = color



        self.tour = 1



        self.r = 30

        self.point = self.canvas.create_oval(self.x + 2, self.y + 3, self.x + 70, self.y + 70, fill=color, outline="blue")



    def setColor(self, color):

        self.canvas.itemconfigure(self.point, fill=color)

        self.color = color





class Board(Canvas):

    def __init__(self, master=None):

        Canvas.__init__(self)

        self.configure(width=500, height=400, bg="blue")



        self.player = 1

        self.color = "yellow"

        self.p = []

        self.perm = True



        for i in range(0, 350, int(400 / 6)): #Setting the rows

            whitespots = []

            for j in range(0, 440, int(500 / 7)): #Setting the columns

                whitespots.append(Point(j, i, self))



            self.p.append(whitespots)



        self.bind("<Button-1>", self.colorswitch)



    def colorswitch(self, event):

        if self.perm:

            col = int(event.x / 71)

            lig = 0



            lig = 0

            while lig < len(self.p):

                if self.p[0][col].color == "red" or self.p[0][0].color == "yellow":

                    break



                if self.p[lig][col].color == "red" or self.p[lig][col].color == "yellow":

                    self.p[lig - 1][col].setColor(self.color)

                    break



                elif lig == len(self.p) - 1:

                    self.p[lig][col].setColor(self.color)

                    break



                if self.p[lig][col].color != "red" and self.p[lig][col].color != "yellow":

                    lig += 1



            if self.player == 1:

                self.player = 2

                info.t.config(text="Reds Turn")

                self.color = "red"



            elif self.player == 2:

                self.player = 1

                info.t.config(text="Yellows Turn")

                self.color = "yellow"



            self.Horizontal()

            self.Vertical()

            self.Diagonal1()

            self.Diagonal2()



    def Horizontal(self):

        i = 0

        while (i < len(self.p)):

            j = 0

            while (j < 3):

                if (self.p[i][j].color == self.p[i][j + 1].color == self.p[i][j + 2].color == self.p[i][

                    j + 3].color == "red"):

                    info.t.config(text="RED IS THE WINNER")

                    self.perm = False

                    break

                elif (self.p[i][j].color == self.p[i][j + 1].color == self.p[i][j + 2].color == self.p[i][

                    j + 3].color == "yellow"):

                    info.t.config(text="YELLOW IS THE WINNER")

                    self.perm = False

                    break

                j += 1

            i += 1



    def Vertical(self):

        i = 0

        while (i < 3):

            j = 0

            while (j < len(self.p[i])):

                if (self.p[i][j].color == self.p[i + 1][j].color == self.p[i + 2][j].color == self.p[i + 3][

                    j].color == "red"):

                    info.t.config(text="RED IS THE WINNER")

                    self.perm = False

                    break

                elif (self.p[i][j].color == self.p[i + 1][j].color == self.p[i + 2][j].color == self.p[i + 3][

                    j].color == "yellow"):

                    info.t.config(text="YELLOW IS THE WINNER")

                    self.perm = False

                    break

                j += 1

            i += 1



    def Diagonal1(self):

        i = 0

        while (i < 3):

            j = 0

            while (j < 3):

                if (self.p[i][j].color == self.p[i + 1][j + 1].color == self.p[i + 2][j + 2].color == self.p[i + 3][

                    j + 3].color == "red"):

                    info.t.config(text="RED IS THE WINNER")

                    self.perm = False

                    break

                elif (self.p[i][j].color == self.p[i + 1][j + 1].color == self.p[i + 2][j + 2].color == self.p[i + 3][

                    j + 3].color == "yellow"):

                    info.t.config(text="YELLOW IS THE WINNER")

                    self.perm = False

                    break

                j += 1

            i += 1



    def Diagonal2(self):

        i = 0

        while (i < 3):

            j = len(self.p[i]) - 1

            while (j > len(self.p) - 4):

                if (self.p[i][j].color == self.p[i + 1][j - 1].color == self.p[i + 2][j - 2].color == self.p[i + 3][

                    j - 3].color == "red"):

                    info.t.config(text="RED IS THE WINNER")

                    self.perm = False

                    break

                elif (self.p[i][j].color == self.p[i + 1][j - 1].color == self.p[i + 2][j - 2].color == self.p[i + 3][

                    j - 3].color == "yellow"):

                    info.t.config(text="YELLOW IS THE WINNER")

                    self.perm = False

                    break

                j -= 1

            i += 1





root = Tk()

root.geometry("800x550")

root.title("CONNECT FOUR")



info = Info(root)

info.grid(row=0, column=0)



t = Board(root)

t.grid(row=1, column=0)





def restart():

    global info

    info.t.config(text="")



    info = Info(root)

    info.grid(row=0, column=0)



    t = Board(root)

    t.grid(row=1, column=0)





Button(root, text="RESTART GAME", command=restart).grid(row=2, column=0, pady=30)



root.mainloop()