import random
from variables import *
#---------------------------------------------#

def Rock():
    global PLayerChoice, PcChoice
    PcChoice = random.choice('rps')
    PLayerChoice = 'r'
    check(PLayerChoice, PcChoice)

def Paper():
    global PLayerChoice, PcChoice
    PcChoice = random.choice('rps')
    PLayerChoice = 'p'
    check(PLayerChoice, PcChoice)

def Scissors():
    global PLayerChoice, PcChoice
    PcChoice = random.choice('rps')
    PLayerChoice = 's'
    check(PLayerChoice, PcChoice)

def check(Player, Pc):
    result.delete(0, END)

    if Player == Pc:
        result.insert(END, 'DRAW')

    elif Player == 'r' and Pc == 's':
        result.insert(END, f'You win, Pc choice: "scissors", Your choice: "rock"')

    elif Player == 'r' and Pc == 'p':
        result.insert(END, f'Pc win, Pc choice: "paper", Your choice: "rock"')

    elif Player == 'p' and Pc == 'r':
        result.insert(END, f'You win, Pc choice: "rock", Your choice: "paper"')

    elif Player == 'p' and Pc == 's':
        result.insert(END, f'Pc win, Pc choice: "scissors", Your choice: "paper"')

    elif Player == 's' and Pc == 'p':
        result.insert(END, f'You win, Pc choice: "paper", Your choice: "scissors"')

    elif Player == 's' and Pc == 'r':
        result.insert(END, f'Pc win, Pc choice: "rock", Your choice: "scissors"')