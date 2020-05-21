from tkinter import *
#############################


root = Tk()
root.title('Covid-19 Tracker ~ Program by Yovan')
root.geometry('800x600')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


button = Button(root, text = "testing")
button.pack()

menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Tentang", command=donothing)
helpmenu.add_command(label="Keluar", command=root.quit)

root.config(menu=menubar)

root.mainloop()