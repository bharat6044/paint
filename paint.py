from tkinter import *


class Paint():
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry('800x520')
        self.root.configure(background="white")
        self.root.resizable(0, 0)


        self.pen_colour = 'black'




        # colour frame
        self.colour_frame = LabelFrame(self.root, text="Color", font={'arial', 15}, bd=5, relief=RIDGE, bg="white")
        self.colour_frame.place(x=0, y=0, width=70, height=185)

        colour_list = ['#ff0000', '#ff4dd2', '#ffff33', '#000000', '#0066ff', '#660033', '#4dff4d', '#b300b3',
                       '#00ffff', '#808080', '#99ffcc', '#336600']
        i, j = 0, 0
        for colour in colour_list:
            Button(self.colour_frame, bg=colour, bd=2, command= lambda col = colour: self.color(col), relief=RIDGE).grid(row=i, column=j)
            j += 1
            if j == 2:
                j = 0
                i += 1

        # eraser
        self.eraser = Button(self.root, text="Eraser", command=self.erase, relief=RIDGE)
        self.eraser.place(x=0, y=187)

        # clear
        self.clear = Button(self.root, text="Clear", command=self.clear, relief=RIDGE)
        self.clear.place(x=0, y=217)

        # save
        self.save = Button(self.root, text="Save", command=None, relief=RIDGE)
        self.save.place(x=0, y=247)

        # canvas
        self.canvas_button = Button(self.root, text="Canvas", command=None, relief=RIDGE)
        self.canvas_button.place(x=0, y=277)

        # size
        self.size = LabelFrame(self.root, text="Size", font={'arial', 15}, bd=5, relief=RIDGE, bg="white")
        self.size.place(x=0, y=307, width=70, height=195)

        #zoom
        self.zoom = Scale(self.size, orient=VERTICAL, from_=50, to=0, length=165)
        self.zoom.set(50)
        self.zoom.grid(row=0, column=1, padx=15)

        #canvas
        self.canvas = Canvas(self.root, relief=GROOVE, bg="white", bd=5, height=500, width=700)
        self.canvas.place(x=80, y=0)

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, width=self.zoom.get(), fill=self.pen_colour,outline=self.pen_colour)

    def color(self,colour):
        self.pen_colour = colour

    def clear(self):
        self.canvas.delete("all")

    def erase(self):
        self.pen_colour = "white"






if __name__ == "__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()

