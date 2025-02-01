import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("800x800")

label1=tk.Label(root, text="Enter total amount:")
label1.place(x=300,y=100)

input1=tk.Entry()
input1.place(x=300,y=150)

label2=tk.Label(root, text="Here are number of notes for each denomination:")
label2.place(x=200,y=300)

de2000label=tk.Label(root, text="2000")
de2000label.place(x=250,y=375)
de2000entry=tk.Entry()
de2000entry.place(x=400,y=375)

de500label=tk.Label(root, text="500")
de500label.place(x=250,y=450)
de500entry=tk.Entry()
de500entry.place(x=400,y=450)

de100label=tk.Label(root, text="100")
de100label.place(x=250,y=525)
de100entry=tk.Entry()
de100entry.place(x=400,y=525)

def calculator():
    try:
        global amount
        amount=int(input1.get())
        note2000= amount // 2000
        amount %= 2000
        note500= amount // 500
        amount %= 500
        note100= amount // 100

        de2000entry.delete(0, tk.END)
        de500entry.delete(0, tk.END)
        de100entry.delete(0, tk.END)

        de2000entry.insert(tk.END, str(note2000))
        de500entry.insert(tk.END, str(note500))
        de100entry.insert(tk.END, str(note100))
    except:
        messagebox.showerror('Error', 'Please enter a valid number')

button1=tk.Button(root, text="Calculate", command=calculator)
button1.place(x=300,y=200)

button2=tk.Button(root, text="Let's get started")

root.mainloop()