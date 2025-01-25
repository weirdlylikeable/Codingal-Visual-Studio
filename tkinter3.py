import tkinter as tk
from PIL import Image, ImageTk

root= tk.Tk()
root.title("Image")
root.geometry("500x500")

upload=Image.open("frog.jpeg")

uploadimage=ImageTk.PhotoImage(upload)

label=tk.Label(root ,image=uploadimage, width=200, height=200)
label.place(x=100, y=100)
label1=tk.Label(root, text="This is an image of a frog")
label1.place(x=100, y=400)

root.mainloop()