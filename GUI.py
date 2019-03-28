'''

        Author: Shane Cincotta
        Last Edited: 10/22/18

'''
import tkinter
from tkinter import *

def decimal_to_binary():
    binary_entry2.delete(0, 30)  #Making sure the whole entry gets deleted
    binary = []
    valid_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for n in decimal_entry2.get():
        if n not in valid_numbers:
            decimal_entry2.delete(0, 30)
            raise Exception(decimal_entry2.insert(0, "Please enter an Integer"))

    decimal = int(decimal_entry2.get())

    for i in range(12, -1, -1):  #Controls the bit count, currently set for an 13 bit number
        if decimal == 0:
            binary.append(0)
        elif decimal-(2**i) >= 0:
            decimal -= 2**i
            binary.append(1)
        else:
            binary.append(0)

    binary = "".join(map(str, binary))  #Making the list of ints into a single string.
    binary_entry2.insert(0, binary)

def binary_to_decimal():
    decimal_entry.delete(0, 30)
    valid_numbers = ["0", "1"]
    for n in binary_entry.get():
        if n not in valid_numbers:
            binary_entry.delete(0, 30)
            raise Exception(binary_entry.insert(0, "Please enter a bit"))

    binary = binary_entry.get()
    decimal = 0
    exponent = 0
    binary_number = str(binary)  #First making binary_number a str so I can split it up by term
    binary_list = list(binary_number)

    binary_list = [int(i) for i in binary_list]  #Making each of those terms an int after I split them
    binary_list = binary_list[::-1]  #Binary is read from right to left

    for i in binary_list:
        if i == 1:
            decimal += 2**exponent
        exponent += 1

    decimal_entry.insert(0, decimal)

####################################################################################################################

app = tkinter.Tk()
app.title("A Simple Converter")
app.config(bg="#000000")
app.geometry("900x450")

background = PhotoImage(file = "C:\\Users\\Shane\\PycharmProjects\\code.png")
background_label = Label(image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

binary_to_decimal_Converter_title = Label(text="Binary to Decimal Converter", relief=RAISED, bd=5, fg="#00ff00", bg="#000000", font=("terminal", 22, "bold"), pady=5)
binary_to_decimal_Converter_title.grid(row=0, column=1)

binary_label = Label(text="Binary Number", relief=RAISED, bd=4, fg="#00ff00", bg="#000000")
binary_label.config(font=("terminal", 20)) #Necessary to change the size of font on label
binary_label.grid(row=1, column=0, padx=2, sticky=W)

decimal_label = Label(text="Decimal Number", relief=RAISED, bd=4, fg="#20C20E", bg="#000000")
decimal_label.config(font=("terminal", 20))  #Necessary to change the size of font on label
decimal_label.grid(row=2, column=0, padx=2, sticky=W)

binary_entry = Entry(width=24, font=("courier", 24), bg="#000000", fg="#00ff00")
binary_entry.grid(row=1, column=1, padx=5, pady=10)
binary_entry.insert(0,"Enter a Binary Number")

decimal_entry = Entry(width=24, font=("courier", 24), bg="#000000", fg="#00ff00")
decimal_entry.grid(row=2, column=1, pady=10)

binary_convert_button = Button(text="Convert", command=binary_to_decimal, bd=3, fg="#00ff00", bg="#000000", activebackground="#00ff00", activeforeground="#000000")
binary_convert_button.config(font=("terminal", 14))
binary_convert_button.grid(row=1, column=2)

####################################################################################################################

decimal_to_binary_Converter_title = Label(text="Decimal to Binary Converter", relief=RAISED, bd=5, font=("terminal", 22, "bold"), pady=5, fg="#00ff00", bg="#000000")
decimal_to_binary_Converter_title.grid(row=3, column=1)

decimal_label2 = Label(text="Decimal Number", relief=RAISED, bd=4, fg="#00ff00", bg="#000000")
decimal_label2.config(font=("terminal", 20)) #Necessary to change the size of font on label
decimal_label2.grid(row=4, column=0, padx=2, sticky=W)

binary_label2 = Label(text="Binary Number", relief=RAISED, bd=4, fg="#00ff00", bg="#000000")
binary_label2.config(font=("terminal", 20)) #  Necessary to change the size of font on label
binary_label2.grid(row=5, column=0, padx=2, sticky=W)

decimal_entry2 = Entry(width=24, font=("Courier", 24), fg="#00ff00", bg="#000000")
decimal_entry2.grid(row=4, column=1, pady=10)
decimal_entry2.insert(0, "Enter a Decimal Number")

binary_entry2 = Entry(width=24, font=("courier", 24), fg="#00ff00", bg="#000000")
binary_entry2.grid(row=5, column=1, pady=10)

decimal_convert_button = Button(text="Convert", command=decimal_to_binary, bd=3, fg="#00ff00", bg="#000000", activebackground="#00ff00", activeforeground="#000000")
decimal_convert_button.config(font=("terminal", 14))
decimal_convert_button.grid(row=4, column=2)

exit_button = Button(text="Exit", command=app.destroy, width=8, bd=3, fg="#00ff00", bg="#000000", activebackground="#00ff00", activeforeground="#000000")
exit_button.config(font=("terminal", 14))
exit_button.grid(row=6, column=0, sticky=W)

app.mainloop()
