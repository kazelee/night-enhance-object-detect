from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def afterpressed():
    if messagebox.askokcancel('Tips', 'OK?'):
        btn.state()
        print('OK!')
    else:
        print('NO!')


root = Tk()
btn = Button(root, text='Press', command=afterpressed)
btn.pack()
# btn.bind('<Button-1>', afterpressed)
root.mainloop()
