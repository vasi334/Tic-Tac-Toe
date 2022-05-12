from tkinter import *

root = Tk()
root.title('Tic Tac Toe')
root.geometry('342x482')

player = True

# functions

list_of_choices = [
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' '
]


def new_window(number):
    top = Toplevel()
    lab = Label(top, text=number + ' won!')
    lab.pack()


def add_to_list(nr):
    if player:
        list_of_choices[nr] = 'X'
    else:
        list_of_choices[nr] = '0'


def check_won():
    if list_of_choices[0] == list_of_choices[1] == list_of_choices[2] and list_of_choices[0] != ' ':
        if list_of_choices[0] == 'X':
            disable_buttons()
            new_window('X')
        else:
            disable_buttons()
            new_window('0')
    elif list_of_choices[0] == list_of_choices[3] == list_of_choices[6] and list_of_choices[0] != ' ':
        if list_of_choices[0] == 'X':
            disable_buttons()
            new_window('X')
        else:
            disable_buttons()
            new_window('0')
    elif list_of_choices[0] == list_of_choices[4] == list_of_choices[8] and list_of_choices[0] != ' ':
        if list_of_choices[0] == 'X':
            disable_buttons()
            new_window('X')
        else:
            disable_buttons()
            new_window('0')
    elif list_of_choices[2] == list_of_choices[4] == list_of_choices[6] and list_of_choices[2] != ' ':
        if list_of_choices[2] == 'X':
            disable_buttons()
            new_window('X')
        else:
            disable_buttons()
            new_window('0')
    elif list_of_choices[6] == list_of_choices[7] == list_of_choices[8] and list_of_choices[6] != ' ':
        if list_of_choices[6] == 'X':
            disable_buttons()
            new_window('X')
        else:
            disable_buttons()
            new_window('0')
    elif list_of_choices[2] == list_of_choices[5] == list_of_choices[8] and list_of_choices[2] != ' ':
        if list_of_choices[2] == 'X':
            disable_buttons()
            new_window('X')
        else:
            disable_buttons()
            new_window('0')


def press_btn(number, btn):
    global player
    if player:
        if btn['text'] == ' ':
            btn.config(text='X')
            btn.config(state=DISABLED)
            add_to_list(number)
            check_won()
            player = False
    else:
        if btn['text'] == ' ':
            btn.config(text='0')
            btn.config(state=DISABLED)
            add_to_list(number)
            check_won()
            player = True


def disable_buttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


# create buttons

btn1 = Button(root, text=' ', command=lambda: press_btn(0, btn1))
btn1.grid(row=0, column=0)
btn1.config(height=10, width=15)

btn2 = Button(root, text=' ', command=lambda: press_btn(1, btn2))
btn2.grid(row=0, column=1)
btn2.config(height=10, width=15)

btn3 = Button(root, text=' ', command=lambda: press_btn(2, btn3))
btn3.grid(row=0, column=2)
btn3.config(height=10, width=15)

btn4 = Button(root, text=' ', command=lambda: press_btn(3, btn4))
btn4.grid(row=1, column=0)
btn4.config(height=10, width=15)

btn5 = Button(root, text=' ', command=lambda: press_btn(4, btn5))
btn5.grid(row=1, column=1)
btn5.config(height=10, width=15)

btn6 = Button(root, text=' ', command=lambda: press_btn(5, btn6))
btn6.grid(row=1, column=2)
btn6.config(height=10, width=15)

btn7 = Button(root, text=' ', command=lambda: press_btn(6, btn7))
btn7.grid(row=2, column=0)
btn7.config(height=10, width=15)

btn8 = Button(root, text=' ', command=lambda: press_btn(7, btn8))
btn8.grid(row=2, column=1)
btn8.config(height=10, width=15)

btn9 = Button(root, text=' ', command=lambda: press_btn(8, btn9))
btn9.grid(row=2, column=2)
btn9.config(height=10, width=15)

root.mainloop()
