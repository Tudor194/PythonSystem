from UseCases.UseCaseTRAINING import *
# import os
import tkinter as tk

window = tk.Tk()
window.title("Widget")

text = tk.Text(window)
text.insert(tk.END, "print(1)"'\n')
text.insert(tk.END, "x = 10"'\n')

text.config(state = "disabled")
text.pack()

window.mainloop()

f = open("UseCaseTRAINING.py", "r")
cod = f.read()
f.close()
print(cod)

#
# directory = "D:\PythonSystem\UseCases"
# files = os.listdir(directory)
#
# listbox = tk.Listbox(window)
#
# for file in files:
#     extension = os.path.splitext(file)[1]
#     if extension == ".py":
#         listbox.insert(tk.END, file)
#
# listbox.pack()
#
# window.mainloop()

#UseCaseTRAINING.Execute()
with open("UseCaseTRAINING.py") as f:
    exec(f.read())