from tkinter import *

w = Tk()
w.geometry('300x500')
w.configure(bg='#141414')


def bttn(x,y,text,bcolor,fcolor,cmd):

    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor

    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor

    mybutton=Button(w,width=42,height=2,text=text,fg=bcolor,bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,command=cmd,)

    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)

def cmd():
    print('You clicked A C E R')

def cmd1():
    print('You clicked A P P L E')

def cmd2():
    print('You clicked D E L L')

def cmd3():
    print('You clicked A S U S')



bttn(0,0,"A C E R", '#ffcc66','#141414',cmd)
bttn(0,37,"A P P L E", '#ffcc66','#141414',cmd1)
bttn(0,74,"D E L L", '#ffcc66','#141414',cmd2)
bttn(0,111,"A S U S", '#ffcc66','#141414',cmd3)
bttn(0,148,"S A M S U N G", '#ffcc66','#141414',cmd3)





w.mainloop()