from tkinter import *
from PIL import ImageTk
import subprocess

def open_bus_window():
    subprocess.Popen(['python', 'bus.py'])
def open_Static_window():
    subprocess.Popen(['python', 'static.py'])    

fenetre = Tk()
fenetre.title('Application Gestion De Location De Bus')
titre = Label(fenetre, text="Gestion De Location De Bus")
titre.pack()

fenetre.config(background="#dcdde1")
fenetre.geometry("1000x700+250+0")


Panal_frame = Frame(fenetre, width=300, height=800, bg='#dcdde1')
Panal_frame.place(x=0, y=10)


bus_image = PhotoImage(file='bus-lane.png')
Bus_BTN=Button(fenetre, image=bus_image, text='', width=280, height=220, bg='#f5f6fa', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=open_Static_window)
Bus_BTN.place(x=10, y=15)

Exit_image = PhotoImage(file='delete.png')
Exit_BTN=Button(fenetre, image=Exit_image, text='', width=280, height=220, bg='#f5f6fa', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=quit)
Exit_BTN.place(x=10, y=240)

Static_image = PhotoImage(file='analytics.png')
Static_BTN=Button(fenetre, image=Static_image, text='', width=280, height=220, bg='#f5f6fa', fg='#1e272e', font=('Calibri (Body)', 12, 'bold'), cursor='hand2', bd=0, command=open_bus_window)
Static_BTN.place(x=10, y=465)





fenetre.mainloop()




