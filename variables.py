from tkinter import *


root = Tk()
root.resizable(height=False, width=False)
root.geometry('500x350')
root.title('Rock Paper Scissors')
#---------------------------------------------#
canva = Canvas(root, width=500, height=500, bg='orange')
frame = Frame(root, bg='orange')
title = Label(frame, text='Rock | Paper | Scissors', bg='orange', font='Arial, 30', foreground='yellow')

#---------------------------------------------#
resultLabel = Label(frame, text='Result', bg='orange', fg='yellow', font='Arial, 35')
result = Entry(frame, width=500, font='Arial, 14')
result.insert(END, '')


