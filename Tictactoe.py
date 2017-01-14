rom tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import simpledialog as SimpleDialog
import random

import sys
import os

def bloquear_tablero():
    for i in range(0,9):
        lista_btn[i].config(state="disable")

def iniciar_juego():

    for i in range(0,9):

        lista_btn[i].config(state="normal")
        lista_btn[i].config(bg="lightblue")
        lista_btn[i].config(text="")
        tab[i] = "N"

    global nombrejg1, nombrejg2
    nombrejg1  = SimpleDialog.askstring("Jugador","Escribe el nombre del jugador 1: ")
    nombrejg2 = SimpleDialog.askstring("Jugador", "Escribe el nombre del jugador 2: ")
    turnojg.set("Turno: " + nombrejg1)

def cambiar(num):
    global cont, turno, turnojg, nombrejg1, nombrejg2

    if tab[num] == "N" and turno == 0:
        lista_btn[num].config(text="X")
        lista_btn[num].config(bg="white")
        tab[num] = "X"
        turno = 1
        cont += 1
        turnojg.set("Turno: " + nombrejg2)

    elif tab[num] == "N" and turno == 1:
        lista_btn[num].config(text="O")
        lista_btn[num].config(bg="lightgreen")
        tab[num] = "O"
        turno = 0
        cont += 1
        turnojg.set("Turno: " + nombrejg1)

    lista_btn[num].config(state="disable")
    ganar(lista_btn)

def ganar(botones):
    global m_x, m_o

    if (btn0.cget("text") == "O" and btn1.cget("text") == "O" and btn2.cget("text") == "O" or
        btn3.cget("text") == "O" and btn4.cget("text") == "O" and btn5.cget("text") == "O" or
        btn6.cget("text") == "O" and btn7.cget("text") == "O" and btn8.cget("text") == "O" or
        btn2.cget("text") == "O" and btn4.cget("text") == "O" and btn6.cget("text") == "O" or
        btn0.cget("text") == "O" and btn4.cget("text") == "O" and btn8.cget("text") == "O" or
        btn2.cget("text") == "O" and btn5.cget("text") == "O" and btn8.cget("text") == "O"):
        root.bell()
        MessageBox.showinfo("Ganador", "Ganaste Jug:  " + nombrejg2)
        if MessageBox.askyesno("Ahora que","Jugar Otra vez?"):
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            quit()

    elif (btn0.cget("text") == "X" and btn1.cget("text") == "X" and btn2.cget("text") == "X" or
        btn3.cget("text") == "X" and btn4.cget("text") == "X" and btn5.cget("text") == "X" or
        btn6.cget("text") == "X" and btn7.cget("text") == "X" and btn8.cget("text") == "X" or
        btn2.cget("text") == "X" and btn4.cget("text") == "X" and btn6.cget("text") == "X" or
        btn0.cget("text") == "X" and btn4.cget("text") == "X" and btn8.cget("text") == "X" or
        btn2.cget("text") == "X" and btn5.cget("text") == "X" and btn8.cget("text") == "X"):
        root.bell()
        MessageBox.showinfo("Ganador", "Ganaste Jug:  " + nombrejg1)
        if MessageBox.askyesno("Ahora que","Jugar Otra vez?"):
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            quit()



root = Tk()

root.geometry("485x520")
root.title("X-0 Basico")
root.resizable(0,0)


nombrejg1 = ""
nombrejg2 = ""

lista_btn = []
tab = []
turnojg = StringVar()
turno = 0
cont = 0
m_x = "X"
m_o = "O"

for i in range(0,9):
    tab.append("N")

#Crear los 9 botones para el tablero
btn0 = Button(root,width=13,height=6,command=lambda:cambiar(0))
lista_btn.append(btn0)
btn0.place(x=0,y=0)

btn1 = Button(root,width=13,height=6,command=lambda:cambiar(1))
lista_btn.append(btn1)
btn1.place(x=120,y=0)

btn2 = Button(root,width=13,height=6,command=lambda:cambiar(2))
lista_btn.append(btn2)
btn2.place(x=240,y=0)

btn3 = Button(root,width=13,height=6,command=lambda:cambiar(3))
lista_btn.append(btn3)
btn3.place(x=0,y=140)

btn4 = Button(root,width=13,height=6,command=lambda:cambiar(4))
lista_btn.append(btn4)
btn4.place(x=120,y=140)

btn5 = Button(root,width=13,height=6,command=lambda:cambiar(5))
lista_btn.append(btn5)
btn5.place(x=240,y=140)

btn6 = Button(root,width=13,height=6,command=lambda:cambiar(6))
lista_btn.append(btn6)
btn6.place(x=0,y=280)

btn7 = Button(root,width=13,height=6,command=lambda:cambiar(7))
lista_btn.append(btn7)
btn7.place(x=120,y=280)

btn8 = Button(root,width=13,height=6,command=lambda:cambiar(8))
lista_btn.append(btn8)
btn8.place(x=240,y=280)

turno_act = Label(root,textvariable=turnojg).place(x=200,y=20)
bloquear_tablero()
iniciar = Button(root, bg="#006", fg="white",text="Iniciar Juego",width=15,height=3,command=iniciar_juego).place(x=120, y=400)
ganar(lista_btn)

root.mainloop()
