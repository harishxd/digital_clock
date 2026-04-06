#creating a digital clock
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x300")

def update_time():
    string = strftime("%H:%M:%S %p\n%D")
    label.config(text=string)
    label.after(1000, update_time)

def resize_font(event):
    if event.height < 100:
        return
    new_size = int(event.height / 5)
    label.config(font=("calibri", new_size, "bold"))

label = tk.Label(root, font=("calibri", 50, "bold"),bg="black", fg="lime")
label.pack(expand=True, fill='both')



root.bind("<Configure>", resize_font)

update_time()
root.mainloop()