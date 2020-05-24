from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def getName():
    name=''
    i=1
    while i<=10:
        j=random.randint(1,10)
        random_num=str(int(random.randrange(1,999)))
        random_char=chr(int(random.randrange(97,122)))
        name+=random_char
        if j%3==0:
            name+=random_num
        i+=1
    return name

def giveName(*args):
    try:
        global value
        name = StringVar()
        value = int(n.get())
        global inframe
        global str_list 
        str_list = []
        inframe = ttk.Frame(mainframe,padding = "5 5 5 5")
        inframe.grid(column = 0,row = 1)
        inframe.columnconfigure(0,weight = 1)
        for i in range(0,value):
            global stronk
            stronk = getName()
            lbl = ttk.Label(inframe,text = stronk)
            lbl.grid(column = 0,row = i,padx = 5,pady = 5)
            str_list.append(stronk)
    except ValueError:
        pass
    root.bind('<BackSpace>',clear)

def clear(*args):
    n.set('')
    inframe.grid_remove()

def save_to_file():
    name = "Random_text_"+getName()+str(random.randint(1,1000))+".txt"
    with open(name,'w') as save:
        for i in range(0,value):
            save.write(str_list[i])
            save.write("\n")
        save.close()
    messagebox.showinfo("Done!","File saved as "+ name + " in current folder")

root = Tk()
root.title("Generate random strings")
root.columnconfigure(0,weight = 1)
root.rowconfigure(0,weight = 1)
mainframe = ttk.Frame(root,padding = "5 5 5 5")
mainframe.grid(column = 0,row = 0)
ttk.Label(mainframe,text = "How many strings do you want? ").grid(column = 0,row = 0,padx = 5,pady = 5)
n = StringVar()
text_enter = ttk.Entry(mainframe,textvariable = n)
text_enter.grid(column = 1,row = 0,padx = 5,pady = 5)
btn = ttk.Button(mainframe,text = "Strings",command = giveName)
btn.grid(column = 2,row = 0,padx = 5,pady = 5)
clr = Button(mainframe,text = "Clear",command = clear)
clr.grid(column = 3,row = 0)
root.bind('<Return>',giveName)
save = Button(mainframe,text = "Save to .txt file",command = save_to_file)
save.grid(column = 4,row = 0,padx = 5,pady = 5)
text_enter.focus()
root.mainloop()