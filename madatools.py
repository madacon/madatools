from tkinter import *
from tkinter.messagebox import * 
import webbrowser
import os


# %windir%\system32\mstsc.exe

root = Tk()
root.title("MADATOOLS")
root.iconbitmap("img/batman.ico")
root.geometry("450x500")

# Web open functions
def web_ticket():
    webbrowser.open_new_tab("https://cism-web.es.corpintra.net/cgi-bin/webTickets/webTicket.pl?t=Mbarg WEB Ticket General")

def unify():
    webbrowser.open_new_tab("https://atosunify.service-now.com/unify?id=index")

def cosyma():
    webbrowser.open_new_tab("https://configmgr.smi.corpintra.net/RDWeb/Pages/en-US/default.aspx")

def it_shops():
    webbrowser.open_new_tab("https://itshop.app.corpintra.net/itshop")

def mocha():
    webbrowser.open_new_tab("https://web3270-an23nmt.mf.corpintra.net/")

#cheklist function

def checklist():
    respuesta = askquestion(title="Checklist",
                message="Estas seguro querer abrir el checklist de fin de turno?")
    if respuesta == "no":
        showinfo(title="Checklist fin de turno", message="Presionar aceptar para cancelar la accion" )
    if respuesta == "yes":
        showinfo(title="En proceso", message=" Esta caractetistica se podra utilizar en la siguiente version")

#Open windows app function

def rdp():
    os.system('start %windir%\system32\mstsc.exe')

def asis_rem():
    os.system('start %windir%\system32\msra.exe /offerra')







#top button

boton_top = Button(root, text="MADATOOLS", bg="light Blue", width=25).place(relx=0.1, rely=0.0)

# bottom button

bottom_top = Button(root, text="CHECKLIST", command=checklist, bg="light Blue", width=25).place(relx=0.1, rely=0.7)


#Left button´s

boton_L1 = Button(root, text="Web Ticket", command=web_ticket, bg="light blue", width=10).place(relx=0.1, rely=0.1)
boton_L2 = Button(root, text="Unify Ticket", command=unify, bg="light blue", width=10).place(relx=0.1, rely=0.2)
boton_L3 = Button(root, text="Cosyma", command=cosyma, bg="light blue", width=10).place(relx=0.1, rely=0.3)
boton_L4 = Button(root, text="IT SHOPS", command=it_shops, bg="light blue", width=10).place(relx=0.1, rely=0.4)
boton_L5 = Button(root, text="MOCHA", command=mocha, bg="light blue", width=10).place(relx=0.1, rely=0.5)
boton_L6 = Button(root, text="AD", command=mocha, bg="light blue", width=10).place(relx=0.1, rely=0.6)

#Right button´s

boton_R1 = Button(root, text="Asist Remota", command=asis_rem, bg="light green", width=10).place(relx=0.3, rely=0.1)
boton_R2= Button(root, text="VNC", command=mocha, bg="light green", width=10).place(relx=0.3, rely=0.2)
boton_R3 = Button(root, text="Print Server", command=mocha, bg="light green", width=10).place(relx=0.3, rely=0.3)
boton_R4 = Button(root, text="Remote Desktop", command=rdp, bg="light green", width=10).place(relx=0.3, rely=0.4)
boton_R5 = Button(root, text="Entorno Qsys", command=mocha, bg="light green", width=10).place(relx=0.3, rely=0.5)
boton_R6 = Button(root, text="Spool Qsys", command=mocha, bg="light green", width=10).place(relx=0.3, rely=0.6)




root.mainloop()