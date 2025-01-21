import tkinter as tk

window=tk.Tk()
for i in range(3):
    for j in range(3):
        frame=tk.Frame(master=window,
                       
                        relief=tk.RAISED,
                        borderwidth=2
                        )
        frame.grid(column=j, row=i, padx=5, pady=5)
        colandrow=tk.Label(master=frame,text=f"Row {i}\n Column {j}")
        colandrow.pack()
window.mainloop()