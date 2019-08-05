# Needs to be run from CMD@C:\Users\jondo\Documents\Engineering\Python\pyTest>python pyCanvas_1.py
from Tkinter import *
import psutil

master = Tk()

#Drawing Lines
w = Canvas(master, width=200, height=200)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 200, 100, 0, fill="red", dash=(4,4))

#Writing Text
text = Text(master)
text.insert(INSERT, "Number of CPU's: " + str(psutil.cpu_count()))

text.pack()

#Buttons
b = Button(master,text = "Click")

b.pack()

#__init__
master.mainloop()