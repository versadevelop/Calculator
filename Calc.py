import math
from tkinter import *
from tkinter import font as tkFont

GUI = Tk()
GUI.configure(background="grey")
GUI.title("Calculator")
GUI.resizable(0, 0)
GUI.geometry("350x451")


def button_clear():
    global CalculationVariable
    CalculationVariable = ""
    imported_Text.set("")


def button_click(item):
    global CalculationVariable
    CalculationVariable += str(item)
    imported_Text.set(CalculationVariable)


def button_equal():
    global CalculationVariable
    temp = 0
    try:
        result = str(eval(CalculationVariable))
        if "." in result:
            temp = "{:,}".format(float(result.replace(',', '')))
        else:
            temp = "{:,}".format(int(result.replace(',', '')))
        imported_Text.set(str(temp))

    except ZeroDivisionError:
        imported_Text.set("Division by zero")
        CalculationVariable = ""
    except SyntaxError:
        imported_Text.set("Try Again")
        CalculationVariable = ""
    except ValueError or TypeError:
        imported_Text.set("You fucked up try again")
        CalculationVariable = ""
    try:
        if "," in temp:
            CalculationVariable = str(temp.replace(',', ''))
        else:
            CalculationVariable = str(temp)
    except TypeError:
        imported_Text.set("Bad typo brother")


def button_backspace():
    global CalculationVariable
    text = CalculationVariable[:-1]
    CalculationVariable = text
    imported_Text.set(text)


def button_virus():
    imported_Text.set("Virus Downloading")


def button_oneToX():
    global CalculationVariable
    try:
        result = input_Output_Field.get()
        if "." in result:
            result = 1 / float(result.replace(',', ''))
        else:
            result = 1 / int(result.replace(',', ''))
        imported_Text.set(str(result))
        CalculationVariable = str(result)
    except ValueError:
        imported_Text.set("Try Again")




def button_squareroot():
    global CalculationVariable
    result = input_Output_Field.get()
    try:
        if "." in result:
            a = math.sqrt(float(result.replace(',', '')))
        else:
            a = math.sqrt(int(result.replace(',', '')))
        imported_Text.set(str(a))
        CalculationVariable = str(a)
    except ValueError:
        imported_Text.set("Try Again")




def button_negate():
    global CalculationVariable
    text = "-" + input_Output_Field.get()
    imported_Text.set(text)


CalculationVariable = ""

imported_Text = StringVar()

input_Output_Field_Frame = Frame(GUI, width=350, height=100, bd=0, highlightbackground="white", highlightcolor="green",
                                 highlightthickness=2)
input_Output_Field_Frame.pack(side=TOP)

input_Output_Field = Entry(input_Output_Field_Frame, font=('Times', 30, 'italic'), fg="white",
                           textvariable=imported_Text,
                           width=100, bg="#2e2c2c", bd=0, justify=RIGHT)
input_Output_Field.bind("<Key>", lambda e: "break")

input_Output_Field.grid(row=0, column=0)

input_Output_Field.pack(ipady=25)

buttons_On_frame = Frame(GUI, bg="gray")

buttons_On_frame.pack()

myFont = tkFont.Font(family='Sans Serif', size=10, weight=tkFont.BOLD)

##############################################################################################################
Button(buttons_On_frame, text="%", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_click("%")).grid(row=0, column=0, padx=1, pady=1)

Button(buttons_On_frame, text="  DONT \n PRESS", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_virus()).grid(row=0, column=1, padx=1, pady=1)

Button(buttons_On_frame, text="C", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_clear()).grid(row=0, column=2, padx=1, pady=1)

Button(buttons_On_frame, text="Del", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755",
       cursor="hand2", command=lambda: button_backspace()).grid(row=0, column=3, padx=1, pady=1)

##############################################################################################################

Button(buttons_On_frame, text="1/x", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755",
       cursor="hand2", command=lambda: button_oneToX()).grid(row=1, column=0, padx=1, pady=1)

Button(buttons_On_frame, text="POW", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755",
       cursor="hand2", command=lambda: button_click("**")).grid(row=1, column=1, padx=1, pady=1)

Button(buttons_On_frame, text="SQUARE", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755",
       cursor="hand2", command=lambda: button_squareroot()).grid(row=1, column=2, padx=1, pady=1)

Button(buttons_On_frame, text="/", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_click("/")).grid(row=1, column=3, padx=1, pady=1)

##############################################################################################################

Button(buttons_On_frame, text="7", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(7)).grid(row=2, column=0, padx=1, pady=1)

Button(buttons_On_frame, text="8", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(8)).grid(row=2, column=1, padx=1, pady=1)

Button(buttons_On_frame, text="9", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(9)).grid(row=2, column=2, padx=1, pady=1)

Button(buttons_On_frame, text="*", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_click("*")).grid(row=2, column=3, padx=1, pady=1)

##############################################################################################################

Button(buttons_On_frame, text="4", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(4)).grid(row=3, column=0, padx=1, pady=1)

Button(buttons_On_frame, text="5", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(5)).grid(row=3, column=1, padx=1, pady=1)
Button(buttons_On_frame, text="6", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(6)).grid(row=3, column=2, padx=1, pady=1)

Button(buttons_On_frame, text="-", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_click("-")).grid(row=3, column=3, padx=1, pady=1)

##############################################################################################################

Button(buttons_On_frame, text="1", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(1)).grid(row=4, column=0, padx=1, pady=1)

Button(buttons_On_frame, text="2", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(2)).grid(row=4, column=1, padx=1, pady=1)

Button(buttons_On_frame, text="3", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(3)).grid(row=4, column=2, padx=1, pady=1)

Button(buttons_On_frame, text="+", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755", cursor="hand2",
       command=lambda: button_click("+")).grid(row=4, column=3, padx=1, pady=1)

##############################################################################################################

Button(buttons_On_frame, text="+/-", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_negate).grid(row=5, column=0, padx=1, pady=1)

Button(buttons_On_frame, text="0", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(0)).grid(row=5, column=1, padx=1, pady=1)
Button(buttons_On_frame, text=",", font=myFont, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
       command=lambda: button_click(".")).grid(row=5, column=2, padx=1, pady=1)

Button(buttons_On_frame, text="=", font=myFont, fg="white", width=10, height=3, bd=0, bg="#555755",
       cursor="hand2", command=lambda: button_equal()).grid(row=5, column=3, padx=1, pady=1)

GUI.mainloop()
