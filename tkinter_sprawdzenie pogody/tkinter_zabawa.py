import tkinter.filedialog
from tkinter import *


def nouveau():
    text1.delete(1.0, tkinter.END)


def ouvrir():
    file = tkinter.filedialog.askopenfile(mode='r')
    fileContents = file.read()
    text1.delete(1.0, END)
    text1.insert(1.0, fileContents)


def save():
    file = tkinter.filedialog.asksaveasfile(mode='w')
    textoutput = text1.get(1.0, END)
    file.write(textoutput.rstrip())
    file.write('\n')


fenetre = Tk()

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouveau", command=nouveau)
menu1.add_command(label="Ouvrir", command=ouvrir)
menu1.add_command(label="Enregistrer", command=save)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

text1 = Text(fenetre, width=100, height=300).pack(side=BOTTOM, padx=30, pady=30)

fenetre.config(menu=menubar)
fenetre.mainloop()