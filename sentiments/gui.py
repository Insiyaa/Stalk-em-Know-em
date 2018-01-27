import tkinter as tk

window = tk.Tk()
window.title("Sentiments")
window.geometry('400x400')

title = tk.Label(text="Welcome to sentiments")
title.grid(column=0, row=0)

button = tk.Button(text="CLick me!")
button.grid(column=0, row=1)

entry_f1 = tk.Entry()
entry_f1.grid(column=0, row=2)

text_f = tk.Text(master=window, height=30, width=30)
text_f.grid(column=0, row=3)

window.mainloop()
