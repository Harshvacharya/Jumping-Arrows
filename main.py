from tkinter import *
from tkinter.messagebox import *

class Bu():
    def __init__(self, root, text, col, c):
        self.text = text
        self.col = col
        self.root = root
        self.c = c
        self.f = "white"
        self.bu = Button(root, text=self.text, font="Arial 12", command=self.ontouch, width=3, bg=self.c, fg="white")
        self.bu.grid(row=1, column=self.col, pady=30)

    def reset(self):
        r = self.root
        r.b1.col = 1
        r.b2.col = 2
        r.b3.col = 3
        r.b4.col = 4
        r.b5.col = 5
        r.b6.col = 6
        r.b7.col = 7
        r.b1.bu.grid(column=1)
        r.b2.bu.grid(column=2)
        r.b3.bu.grid(column=3)
        r.b4.bu.grid(column=4)
        r.b5.bu.grid(column=5)
        r.b6.bu.grid(column=6)
        r.b7.bu.grid(column=7)
        self.bb.grid_forget()
        self.bb1.grid_forget()

    def ontouch(self):
        p = self.col
        d = [self.root.b1, self.root.b2, self.root.b3, self.root.b4, self.root.b5, self.root.b6, self.root.b7]
        if self.text == "→":
            for b in d:
                if b.col == self.col + 1 and b.text == " ":
                    b.bu.grid(row=1, column=self.col)
                    self.bu.grid(row=1, column=b.col)
                    self.col += 1
                    b.col -= 1
                elif b.col == self.col + 2 and b.text == " ":
                    b.bu.grid(row=1, column=self.col)
                    self.bu.grid(row=1, column=b.col)
                    self.col += 2
                    b.col -= 2
        elif self.text == "←":
            for b in d:
                if b.col == self.col - 1 and self.col - 1 > -1 and b.text == " ":
                    b.bu.grid(row=1, column=self.col)
                    self.bu.grid(row=1, column=b.col)
                    self.col -= 1
                    b.col += 1
                elif b.col == self.col - 2 and self.col - 2 > -1 and b.text == " ":
                    b.bu.grid(row=1, column=self.col)
                    self.bu.grid(row=1, column=b.col)
                    self.col -= 2
                    b.col += 2
        self.bu.configure(bg=self.c)
        r = self.root
        if not self.checker():
            if self.wincheck():
                pass
            else:
                a = askyesno(title="Game Over", message='You have no possible moves left!\nDo you want to play again?')
                if not a:
                    quit()
                if a:
                    r.b1.col = 1
                    r.b2.col = 2
                    r.b3.col = 3
                    r.b4.col = 4
                    r.b5.col = 5
                    r.b6.col = 6
                    r.b7.col = 7
                    r.b1.bu.grid(row=1, column=1)
                    r.b2.bu.grid(row=1,column=2)
                    r.b3.bu.grid(row=1,column=3)
                    r.b4.bu.grid(row=1,column=4)
                    r.b5.bu.grid(row=1,column=5)
                    r.b6.bu.grid(row=1,column=6)
                    r.b7.bu.grid(row=1,column=7)

    def colour(self):
        d = [self.root.b1, self.root.b2, self.root.b3, self.root.b4, self.root.b5, self.root.b6, self.root.b7]
        for self in d:
            if self.text == "←":
                if self.col == 1 or self.col == 2 or self.col == 3:
                    self.bu.configure(fg="green")
                else:
                    self.bu.configure(fg='red')
            else:
                if self.col == 7 or self.col == 6 or self.col == 5:
                    self.bu.configure(fg="green")
                else:
                    self.bu.configure(fg="red")
            if self.col == 4:
                self.bu.configure(fg="red")

    def checker(self):
        d = [self.root.b1, self.root.b2, self.root.b3, self.root.b4, self.root.b5, self.root.b6, self.root.b7]
        for self in d:
            if self.text == "→":
                for b in d:
                    if b.col == self.col + 1 and b.text == " ":
                        return True
                    elif b.col == self.col + 2 and b.text == " ":
                        return True
            elif self.text == "←":
                for b in d:
                    if b.col == self.col - 1 and self.col - 1 > -1 and b.text == " ":
                        return True
                    elif b.col == self.col - 2 and self.col - 2 > -1 and b.text == " ":
                        return True
        return False

    def wincheck(self):
        n = 0
        d = [self.root.b1, self.root.b2, self.root.b3, self.root.b4, self.root.b5, self.root.b6, self.root.b7]
        for self in d:
            if self.col == 7 and self.text == "→":
                n += 1
            if self.col == 6 and self.text == "→":
                n += 1
            if self.col == 5 and self.text == "→":
                n += 1
            if self.col == 4 and self.text == " ":
                n += 1
            if self.col == 3 and self.text == "←":
                n += 1
            if self.col == 2 and self.text == "←":
                n += 1
            if self.col == 1 and self.text == "←":
                n += 1
        if n == 7:
            e = showinfo(title="You Won", message="Congratulations!\nYou won the game!")
            self.bb = Button(self.root, text="Reset", command=self.reset)
            self.bb.grid(row=2, column=1, columnspan=7, pady=10)
            # self.bb.pack(anchor='center')

            self.bb1 = Button(self.root, text="Close", command=quit)
            self.bb1.grid(row=3, column=1, columnspan=7, pady=10)
            return True
        else:
            return False

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.b1 = Bu(self, text="→", col=1, c="red")
        self.b2 = Bu(self, text="→", col=2, c="red")
        self.b3 = Bu(self, text="→", col=3, c="red")
        self.b4 = Bu(self, text=" ", col=4, c="white")
        self.b5 = Bu(self, text="←", col=5, c="blue")
        self.b6 = Bu(self, text="←", col=6, c="blue")
        self.b7 = Bu(self, text="←", col=7, c="blue")
        self.t=Label(self, text='Click on ← to move left or jump over one arrow to the left\nClick on → to move right or jump over one arrow to the right.', font=("Arial", 8))
        self.t.grid(row=0, column=1, columnspan=7)

if __name__=="__main__":
    root = Root()
    root.minsize(100, 100)
    root.mainloop()