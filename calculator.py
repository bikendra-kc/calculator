from tkinter import *

expression = ''
c = ''
total=''
a=0
# taking the numbers and adding in form of string
def calc(num):
    global expression
    expression = expression + str(num)
    bikks.set(expression)


# clearing the screen
def clear():
    global expression
    expression = ''
    bikks.set('')


# solving the problem in string
def equalls():
    try:
        global expression
        global total
        total = str(eval(expression))
        bikks.set(total)
        return total
    except:  # if something is wrong in input it wil give error
        bikks.set('error')
        expression = ''

# used to  delete the last variables
def ac():
    global expression
    k=len(expression)
    expression = expression[:k - 1]
    bikks.set(expression)

# used to store the previous answer
def Ans():
    global total
    global expression
    expression=expression + total
    bikks.set(expression)

# main programme with different conditons
while a==0 :
    root = Tk()
    root.title('Simple Calaculator')
    root.iconbitmap('calc.ico')
    root.configure(background='grey')
    root.geometry('450x250')
    bikks = StringVar()
    entry = Entry(root, textvariable=bikks)
    entry.grid(columnspan=4, ipadx=90,ipady=10)
    # creating buttons
    # first row variables with button
    button7 = Button(root, text='7', fg='white', bg='black', command=lambda: calc(7), height=2, width=7)
    button8 = Button(root, text='8', fg='white', bg='black', command=lambda: calc(8), height=2, width=7)
    button9 = Button(root, text='9', fg='white', bg='black', command=lambda: calc(9), height=2, width=7)
    buttonclear = Button(root, text='clear', fg='black', bg='red', command=lambda: clear(), height=2, width=7)
    buttonac = Button(root, text='AC', fg='black', bg='red', command=lambda: ac(), height=2, width=7)

    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)
    buttonclear.grid(row=1, column=3)
    buttonac.grid(row=1, column=4)

    # second row variables with buttons
    button4 = Button(root, text='4', fg='white', bg='black', command=lambda: calc(4), height=2, width=7)
    button5 = Button(root, text='5', fg='white', bg='black', command=lambda: calc(5), height=2, width=7)
    button6 = Button(root, text='6', fg='white', bg='black', command=lambda: calc(6), height=2, width=7)
    buttonMult = Button(root, text='x', fg='white', bg='black', command=lambda: calc('*'), height=2, width=7)
    buttonDiv = Button(root, text='/', fg='white', bg='black', command=lambda: calc( '/'), height = 2, width = 7)

    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    buttonMult.grid(row=2, column=3)
    buttonDiv.grid(row=2, column=4)

    # third row with buttons
    button1 = Button(root, text='1', fg='white', bg='black', command=lambda: calc(1), height=2, width=7)
    button2 = Button(root, text='2', fg='white', bg='black', command=lambda: calc(2), height=2, width=7)
    button3 = Button(root, text='3', fg='white', bg='black', command=lambda: calc(3), height=2, width=7)
    buttonPlus = Button(root, text='+', fg='white', bg='black', command=lambda: calc('+'), height=2, width=7)
    buttonMinus = Button(root, text='-', fg='white', bg='black', command=lambda: calc('-'), height=2, width=7)

    button1.grid(row=3, column=0)
    button2.grid(row=3, column=1)
    button3.grid(row=3, column=2)
    buttonPlus.grid(row=3, column=3)
    buttonMinus.grid(row=3, column=4)

    # fourth row with buttons
    button0 = Button(root, text='0', fg='white', bg='black', command=lambda: calc(0), height=2, width=7)
    buttonDot = Button(root, text='.', fg='white', bg='black', command=lambda: calc('.'), height = 2, width = 7)
    buttonx10 = Button(root, text='x10^10', fg='white', bg='black', command=lambda: calc('*10 ** 10'), height=2, width=7)
    buttonAns = Button(root, text='Ans', fg='white', bg='black', command=lambda: Ans(), height=2, width=7)
    buttonequals = Button(root, text='=', fg='white', bg='black', command=lambda: equalls(), height=2, width=7)

    button0.grid(row=4, column=0)
    buttonDot.grid(row=4, column=1)
    buttonx10.grid(row=4, column=2)
    buttonAns.grid(row=4, column=3)
    buttonequals.grid(row=4, column=4)


    root.mainloop()














