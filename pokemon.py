from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
root = Tk()
root.geometry("700x700")
root.title("Pokemon Game")
root.config(background = "#CBC9AD")

buttonImage = ImageTk.PhotoImage(Image.open("button.jpg"))
Umbreon310 = ImageTk.PhotoImage(Image.open("Umbreon - 310.png"))
Salazzle200 = ImageTk.PhotoImage(Image.open("Salazzle - 200.png"))
Luxray150 = ImageTk.PhotoImage(Image.open("Luxray - 150.png"))
Incineroar250 = ImageTk.PhotoImage(Image.open("Incineroar - 250.png"))
Darkrai180 = ImageTk.PhotoImage(Image.open("Darkrai - 180.png"))
Darkrai110 = ImageTk.PhotoImage(Image.open("Darkrai - 110.png"))
AlolanMarowak200 = ImageTk.PhotoImage(Image.open("Alolan Marowak - 200.png"))

cardsList = [Umbreon310, Salazzle200, Luxray150, Incineroar250, Darkrai180, Darkrai110, AlolanMarowak200]
numberList = [310, 200, 150, 250, 180, 110, 200]

player1 = Label(root, text="Player 1", background = "#CBC9AD", foreground="#DBA159", font=("Comic Sans MS", "20", "bold"))
player2 = Label(root, text="Player 2", background = "#CBC9AD", foreground="#DBA159", font=("Comic Sans MS", "20", "bold"))

number1 = Label(root, background = "#EBB9DF", foreground="#FFFFFF", font=("Comic Sans MS", "20", "bold"))
number2 = Label(root, background = "#EBB9DF", foreground="#FFFFFF", font=("Comic Sans MS", "20", "bold"))

pokemonCard = Label(root, image=Umbreon310)

player1score = 0

def randomCard1():
    randomNum1 = random.randint(0, 6)
    randomCard1 = cardsList[randomNum1]
    randomHealth1 = numberList[randomNum1]
    global player1score
    player1score = randomHealth1 + player1score
    pokemonCard['image'] = randomCard1
    number1['text'] = str(player1score)

player2score = 0

def randomCard2():
    randomNum2 = random.randint(0, 6)
    randomCard2 = cardsList[randomNum2]
    randomHealth2 = numberList[randomNum2]
    global player2score
    player2score = randomHealth2 + player2score
    pokemonCard['image'] = randomCard2
    number2['text'] = str(player2score)
    
button1 = Button(root, image=buttonImage, width=90, height=90, command=randomCard1)
button2 = Button(root, image=buttonImage, width=90, height=90, command=randomCard2)

player1.place(relx=0.1, rely=0.5, anchor=CENTER)
player2.place(relx=0.9, rely=0.5, anchor=CENTER)
number1.place(relx=0.1, rely=0.6, anchor=CENTER)
number2.place(relx=0.9, rely=0.6, anchor=CENTER)
button1.place(relx=0.1, rely=0.73, anchor=CENTER)
button2.place(relx=0.9, rely=0.73, anchor=CENTER)
pokemonCard.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()