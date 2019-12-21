from tkinter import *
def printEntry():
    man = entry
    return man
    
root = Tk()
entry = Entry(root)
entry.grid()

b= Button(root, text="submit", command=printEntry)
b.grid(row=1)

label = Label(root, text="the thing written by you is: ")
label.grid(row=2)

l = Label(root, text=str(man))
l.grid(row=3)

root.mainloop()