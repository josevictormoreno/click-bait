import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random 

screen = tk.Tk()
screen.title("ACEITE!")
screen.geometry("600x600")
screen.configure(background='#ffffff')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, screen.winfo_width() - button_1.winfo_width())
        y = random.randint(0, screen.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('CORRETO!')
def denied():
    button_1.destroy()

margin = Canvas(screen, width=500, bg='#FFFFFF', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(screen, bg='#ffffff', text='O zeviane é um babaca?', fg='#000000', font=('arial', 30, 'bold'))
text_id.pack()
button_1 = tk.Button(screen, text='Não', bg='#909090', bd=3, command=denied, relief=RIDGE, font=('arial', 10, 'bold'))
button_1.pack()
screen.bind('<Motion>', move_button_1)
button_2 = tk.Button(screen, text='Sim', bg='#909090', relief=RIDGE,  bd=3, command=accepted, font=('arial', 10, 'bold') )
button_2.pack()

screen.mainloop()