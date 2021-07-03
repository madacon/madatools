from tkinter import *
from tkinter.messagebox import * 
import webbrowser
import os

root = Tk()
root.title("MADATOOLS")
root.iconbitmap("img/batman.ico")
root.geometry('300x500')
root.configure(bg='#141414')

#animated button function

def bttn(x,y,text,bcolor,fcolor,cmd):

    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor

    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor

    mybutton=Button(root,width=42,height=2,text=text,
                    fg=bcolor,bg=fcolor,border=0,
                    activeforeground=fcolor,activebackground=bcolor,
                    command=cmd,)

    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)


def cmd():
    webbrowser.open_new_tab("https://cism-web.es.corpintra.net/cgi-bin/webTickets/webTicket.pl?t=Mbarg WEB Ticket General")
    
def cmd1():
    webbrowser.open_new_tab("https://atosunify.service-now.com/unify?id=index")
    
def cmd2():
    webbrowser.open_new_tab("https://configmgr.smi.corpintra.net/RDWeb/Pages/en-US/default.aspx")
    
def cmd3():
    webbrowser.open_new_tab("https://itshop.app.corpintra.net/itshop")
    
def cmd4():
    webbrowser.open_new_tab("https://web3270-an23nmt.mf.corpintra.net/")
    
def cmd5():
    os.system('start %windir%\system32\dsa.msc')

def cmd6():
    os.system('start %windir%\system32\msra.exe /offerra')

def cmd7():
    print('You clicked VNC')

def cmd8():
    print('You clicked PRINT SERVER')

def cmd9():
    os.system('start %windir%\system32\mstsc.exe')


def cmd10():
    print('You clicked ENTORNO QSYS')

def cmd11():
    print('You clicked SPOOL QSYS')

def cmd12():
    print('You clicked CHECKLIST')



#color 1
bttn(0,0,"WEB TICKET", '#ffcc66','#141414',cmd)
bttn(0,37,"UNIFY TICKET", '#25dae9','#141414',cmd1)
bttn(0,74,"COSYMA", '#f86263','#141414',cmd2)
bttn(0,111,"IT SHOPS", '#ffa157','#141414',cmd3)
#color 2
bttn(0,148,"MOCHA", '#ffcc66','#141414',cmd4)
bttn(0,185,"ACTIVE DIRECTORY", '#25dae9','#141414',cmd5)
bttn(0,222,"ASISTENCIA REMOTA", '#f86263','#141414',cmd6)
bttn(0,259,"VNC", '#ffa157','#141414',cmd7)
#color 3
bttn(0,296,"PRINT SERVER", '#ffcc66','#141414',cmd8)
bttn(0,333,"REMOTE DESKTOP", '#25dae9','#141414',cmd9)
bttn(0,370,"ENTORNO QSYS", '#f86263','#141414',cmd10)
bttn(0,407,"SPOOL QSYS", '#ffa157','#141414',cmd11)
#color 4
bttn(0,444,"CHECKLIST", '#ffcc66','#141414',cmd12)








root.mainloop()