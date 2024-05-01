from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Endless Pokemon Game")
root.geometry("600x400")

root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open ("greninja.png"))

player1 = Label(root, text= "Player 1", bg= "red", fg= "white")
player1.place(relx =0.1 , rely= 0.3 , anchor= CENTER)

player2 = Label(root, text= "Player 2", bg= "red", fg= "white")
player2.place(relx =0.9 , rely= 0.3 , anchor= CENTER)

player_1_score_label = Label(root, bg= "royal blue", fg= "white")
player_1_score_label.place(relx =0.1 , rely= 0.4 , anchor= CENTER)

player_2_score_label = Label(root, bg= "royal blue", fg= "white")
player_2_score_label.place(relx =0.9 , rely= 0.4 , anchor= CENTER)

player_dice_label = Label(root, bg= "white", fg= "white")
player_dice_label.place(relx =0.5 , rely= 0.5 , anchor= CENTER)

root.mainloop()