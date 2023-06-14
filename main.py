import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random 

screen = tk.Tk()
screen.title("ACEITE!")
screen.geometry("600x600")
screen.configure(background='#ffc8dd')

def move_button(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, screen.winfo_width() - button_1.winfo_width())

margin = Canvas(screen, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label()
button_1 = tk.Button(screen, width=500, bg='#ffc8dd',  height=100, bd=0, highlightthickness=0, relief='ridge')
