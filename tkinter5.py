import tkinter as tk

root=tk.Tk()
root.geometry("400x500")

def topwin():
    top=tk.Toplevel()
    top.geometry("200x100")
    l1=tk.Label(top, text="This is the top window.")
    l1.pack()
    
    top.mainloop()

button=tk.Button(root, text="To show top window", command=topwin)

button.pack()
root.mainloop()