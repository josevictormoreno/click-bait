import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random 

screen = tk.Tk()
screen.title("ACEITE!")
screen.geometry("600x600")
screen.configure(background='#ffc8dd')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, screen.winfo_width() - button_1.winfo_width())

def accepted():
    messagebox.showinfo('OBA!')
def denied():
    button_1.destroy()

margin = Canvas(screen, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(screen, bg='#ffc8dd', text='quer namorar comigo?', fg='#590d2', font=('Arial', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(screen, width=500, bg='#ffc8dd',  height=100, bd=0, highlightthickness=0, relief='ridge')
button_1.pack()
screen.bind('<Motion>', move_button_1)
button_2 = tk.Button(screen, text='Sim', bg='#ffb3c1', relief=RIDGE,  bd=3, command=accepted, font=('Arial', 24, 'bold'))
button_2.pack()

screen.mainloop()