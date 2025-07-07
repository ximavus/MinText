from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Minimal text editor!')
root.geometry("1920x1080")
frm = ttk.Frame(root, padding=10)
frm.grid()
global textarea
textarea = Text(frm, background='black', foreground='white', width=200, height=56)
textarea.grid()
def run():
    exec(textarea.get('1.0', 'end-1c'))
global filename_entry
filename_entry = ttk.Entry(frm)
filename_entry.grid(column=2, row=1)
global filename
filename = ''
def save():
    filename = filename_entry.get()
    print(filename)
    print(textarea.get('1.0', 'end-1c'))
    makefile(filename, textarea.get('1.0', 'end-1c'))
def makefile(name: str, contents: str):
    file = open(name, 'w')
    file.write(contents)
    file.close()
ttk.Button(frm, text="Save", command=save).grid(column=1, row=3)
ttk.Button(frm, text="Run", command=run).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
root.mainloop()
