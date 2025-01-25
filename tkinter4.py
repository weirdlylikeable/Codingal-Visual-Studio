import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("500x500")

def msg():
    messagebox.showwarning("BE AWARE! A virus has been detected in your system.")

button=tk.Button(root, text="Scan for virus", command=msg)
button.pack()

root.mainloop()