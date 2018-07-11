from tkinter import *

window = Tk()

def km_miles():
    miles = float(e1_var.get()) * 1.6
    t1.insert(END,miles)

b1 = Button(window,text="Execute",command=km_miles)  #dont use () after function name since it has to only run on click of button
b1.grid(row=0,column=0)                              # or we can use......   b1.pack()

e1_var = StringVar()
e1 = Entry(window, textvariable = e1_var)
e1.grid(row=0,column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=0,column=3)

window.mainloop()
