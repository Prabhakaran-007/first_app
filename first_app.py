from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    input_value.set(expression)

def equal():
    global expression
    total = str(eval(expression))
    input_value.set(total)
    expression = ""

def clear():
    global expression
    expression = ""
    input_value.set("")


window = Tk()
window.title("Simple Calculator")
window.geometry("265x125")
input_value = StringVar()

expression_field = Entry(window, textvariable=input_value)
expression_field.grid(columnspan=4, ipadx=70)

input_value.set('enter the number')

nine = Button(window, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=1, width=7)
nine.grid(row=2, column=0)

eight = Button(window, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=1, width=7)
eight.grid(row=2, column=1)

seven = Button(window, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=1, width=7)
seven.grid(row=2, column=2)

six = Button(window, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=1, width=7)
six.grid(row=3, column=2)

five = Button(window, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=1, width=7)
five.grid(row=3, column=1)

four = Button(window, text=' 4 ', fg='black', bg='white',   command=lambda: press(4), height=1, width=7)
four.grid(row=3, column=0)

three = Button(window, text=' 3 ', fg='black', bg='white',  command=lambda: press(3), height=1, width=7)
three.grid(row=4, column=2)

two = Button(window, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=1, width=7)
two.grid(row=4, column=1)

one = Button(window, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=1, width=7)
one.grid(row=4, column=0)


zero = Button(window, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=1, width=7)
zero.grid(row=5, column=0)

plus = Button(window, text=' + ', fg='black', bg='white',  command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(window, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(window, text=' * ', fg='black', bg='white',command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(window, text=' / ', fg='black', bg='white',command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(window, text=' = ', fg='black', bg='white', command=equal, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(window, text='Clear', fg='black', bg='white',command=clear, height=1, width=7)
clear.grid(row=5, column='1')

window.mainloop()


