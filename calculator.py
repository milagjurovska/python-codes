import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import SUNKEN

ime=tk.Tk()
ime.title("Calculator")

ramka=tk.Frame(ime, bg="lightgreen", padx=10)
ramka.pack()

vlez=tk.Entry(ramka, relief=SUNKEN, borderwidth=3, width=30)
vlez.grid(row=0, column=0, columnspan=3, ipady=2, ipadx=2)

def click(number):
    current_text = vlez.get()

    if number == ".":
        parts = current_text.split("+") + current_text.split("-") + current_text.split("*") + current_text.split(
            "/") + current_text.split("^")
        last_number = parts[-1] if parts else ""

        if "." in last_number:
            return
    vlez.insert(tk.END, number)

def custom_functions(event):
    try:
        broevi=[]
        operatori=[]
        num=""

        for char in event:
            if char in "+-/*^":
                if num:
                    broevi.append(float(num))
                operatori.append(char)
                num=""
            else:
                num+=char
        if num:
            broevi.append(float(num))

        while "^" in operatori:
            i = operatori.index("^")
            broevi[i] = broevi[i] ** broevi[i + 1]
            del broevi[i + 1]
            del operatori[i]

        while "*" in operatori or "/" in operatori:
            for i, op in enumerate(operatori):
                if op == "*":
                    broevi[i] = broevi[i] * broevi[i + 1]
                    del broevi[i + 1]
                    del operatori[i]
                    break
                elif op == "/":
                    if broevi[i + 1] == 0:
                        return "Error"
                    broevi[i] = broevi[i] / broevi[i + 1]
                    del broevi[i + 1]
                    del operatori[i]
                    break

        while "+" in operatori or "-" in operatori:
            for i, op in enumerate(operatori):
                if op == "+":
                    broevi[i] = broevi[i] + broevi[i + 1]
                    del broevi[i + 1]
                    del operatori[i]
                    break
                elif op == "-":
                    broevi[i] = broevi[i] - broevi[i + 1]
                    del broevi[i + 1]
                    del operatori[i]
                    break

        return broevi[0]


    except:
        return "Error"


def equal():
    expression=vlez.get()
    rezultat=custom_functions(expression)

    if rezultat=="Error":
        messagebox.showinfo("Error", "Syntax Error")
    else:
        vlez.delete(0, tk.END)
        vlez.insert(0, rezultat)

def clear():
    vlez.delete(0, tk.END)

kopchinja=[('1', 1, 0), ('2', 1, 1), ('3', 1, 2),('4', 2, 0), ('5', 2, 1), ('6', 2, 2),('7', 3, 0), ('8', 3, 1), ('9', 3, 2),('.', 4 ,0),('0', 4, 1), ('+', 4, 2), ('-', 5, 0), ('*', 5, 1),('/', 5, 2),("^", 6, 1)]

for txt, r, c in kopchinja:
    tk.Button(ramka, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

tk.Button(ramka, text="AC", padx=15, pady=5, width=3, command=clear).grid(row=6, column=0, columnspan=1, pady=2)
tk.Button(ramka, text="=", padx=15, pady=5, width=3,command=equal).grid(row=6, column=2, columnspan=1, pady=2)

ime.mainloop()
