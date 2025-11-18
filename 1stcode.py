import tkinter as tk
r=tk.Tk()
r.title("drawing pad")
canvas=tk.Canvas(r,width=600,height=400,bg="white")
canvas.pack()
def draw(event):
    x,y=event.x,event.y
    canvas.create_oval(x,y,x+5,y+5,fill="black")

canvas.bind("<B1-Motion>",draw)
r.mainloop()
