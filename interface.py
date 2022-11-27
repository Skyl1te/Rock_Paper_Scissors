from variables import *
from functions import *


canva.pack()
frame.place(relwidth=0.9, relheight=1, relx=0.05, rely=0.05)
title.pack()
#---------------------------------------------#
rockButton = Button(frame, width=17, height=2, bg='darkorange', text='Rock', fg='yellow', command=Rock)
paperButton = Button(frame, width=17, height=2, bg='darkorange',  text='Paper', fg='yellow', command=Paper)
scissorsButton = Button(frame, width=17, height=2, bg='darkorange',  text='Scissors', fg='yellow', command=Scissors)
#---------------------------------------------------------------#
scissorsButton.place(y=110, x=160)
paperButton.place(y=110, x=0)
rockButton.place(y=110, x=320)
#---------------------------------------------------------------#
resultLabel.place(y=190, x=140)
result.place(y=250, height=60)


root.mainloop()