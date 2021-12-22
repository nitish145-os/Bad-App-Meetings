import tkinter as tk

str = window = "Bad App By Nitish Thombre"

root = tk.Tk()

EventButton = tk.Button(root, text="Ëvent")
EventButton.grid(column=1, row=1)


ChatButton = tk.Button(root, text="Chat")
ChatButton.grid(column=2, row=1)

ClassButton = tk.Button(root, text="Calls")
ClassButton.grid(column=3, row=1)

PlayButton = tk.Button(root, text="Play")
PlayButton.grid(column=4, row=1)


root.mainloop()
