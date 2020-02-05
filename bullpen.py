import tkinter
from tkinter import ttk
from tkinter import N, E, W, S


def conversion():
    #実際にはここでt1を元に複雑な処理を行う
    t2 = t1.get() + 0


root = tkinter.Tk()
root.title('test')

frame1 = tkinter.ttk.Frame(root)
label1 = tkinter.ttk.Label(frame1, text = 'test')

t1 = tkinter.StringVar()
t2 = tkinter.StringVar()

entry1 = ttk.Entry(frame1, textvariable = t1)
button1 = ttk.Button(frame1, text = 'OK' , command = conversion )

entry2 = ttk.Entry(frame1, textvariable = t2)

frame1.grid(row=0, column=0, sticky=(N,E,S,W))
label1.grid(row=1, column=1, sticky=E)
entry1.grid(row=1, column=2, sticky=W)
button1.grid(row=2, column=2, sticky=W)

for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
