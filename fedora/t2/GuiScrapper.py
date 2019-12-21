from tkinter import *
import Scrapper

root = Tk()
st=StringVar()

def go():
    def foo():
        var=entry.get()
        a,b,c,d,e=Scrapper.calc(str(var))
        
        if a!=var:
            st.set(a)
        else:   
            st.set("Handle: "+a+"\n"+"Current Rating: "+b+"\n"+"Rank: "+c+"\n"+"Max. Rating: "+d+"\n"+"Max. Rank: "+e)
            
    label = Label(root, text = "Enter your username:")
    entry = Entry(root)
    
    label.grid(row=1)
    entry.grid(row=1, column=1)
    
    b=Button(root, text="Done", command=foo)
    b.grid(row=2)
    ln=Label(root,textvariable=st)
    ln.grid(row=3)
    
    lTitle = Label(root, text = "-:Codeforces Scrapper:-")
    lTitle.grid(row=0)
    
    root.mainloop()

go()
