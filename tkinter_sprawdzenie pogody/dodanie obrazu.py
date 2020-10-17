import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()

img = ImageTk.PhotoImage(Image.open("globus.jpg"))


label = tk.Label(root, image=img)
label.pack()

root.mainloop()
