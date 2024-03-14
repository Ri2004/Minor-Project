# Scientific Calculator using Python Tkinter

from tkinter import *
import numpy as np
from pygame import mixer
import speech_recognition
from PIL import Image, ImageTk
import math

# root is instance of Tk class
root = Tk()

# geometry() is use for give the size of GUI window and 500+50 is for bring the window in center
root.geometry("540x608+500+50")

# title() method is use for give the title of window 
root.title("Scientific Calculator")

# resizable() method is use for fixed the size of window, no one can change the size, that's why width= False and height = False
root.resizable(width=False, height=False)

mixer.init()

def clear():
    entry_obj.delete(0, END)

def back():
    length = len(entry_var.get())-1
    entry_obj.delete(first=length)

def press(string):
    length = len(entry_obj.get())
    
    if entry_obj.get() == '0':
        entry_obj.delete(0, END)
        
    entry_obj.insert(index=length, string=string)

def showMinusSign():
    entry_obj.insert(0, '-')
    

# Arithmetic Operations
def expressionBreak(sign, math_expression):
    expression_value = math_expression.split(sign)
    return expression_value

def scientificCalculation(splittedExpression):
    if splittedExpression[0] == "tan":
        return np.tan(float(splittedExpression[1]))

    elif splittedExpression[0] == "cos":
        return np.cos(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "sin":
        return np.sin(float(splittedExpression[1]))

    elif splittedExpression[0] == "square":
        return np.square(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "sqrt":
        return np.sqrt(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "fac":
        return math.factorial(int(splittedExpression[1]))
    
    elif splittedExpression[0] == "log":
        return np.log10(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "ln":
        return np.log(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "deg":
        return np.degrees(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "rad":
        return np.radians(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "abs":
        return np.absolute(float(splittedExpression[1]))
    
    elif splittedExpression[0] == "1/":
        return np.reciprocal(float(splittedExpression[1]))
    
# equal Function is invoke when equal button is clicked
def equal():
    expression = entry_obj.get()
    clear()
    try:
        if expression.find("(") > 0:
            expression_value = expressionBreak("(", math_expression= expression)
            result = scientificCalculation(expression_value)
            
        elif expression.find("pow") > 0:
            expression_value = expressionBreak("pow",math_expression= expression)
            result = np.power(float(expression_value[0]),float((expression_value[1])))
            
        else:
            # Evaluate the expression using eval() function
            result = eval(expression)
        # Insert the result into the entry field
        entry_obj.insert(0, result)
        
    except Exception as obj:
        entry_obj.insert(0, obj)


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b 

def div(a,b):
    return a/b

def mod(a,b):
    return a%b 

operations = {
    "ADD":add, "ADDITION":add, "PLUS":add, "SUM":add,
    "MINUS":sub, "DIFFERENCE":sub, "SUBTRACT":sub, "SUBTRACTION":sub,
    "MULTIPLY":mul, "MULTIPLICATION":mul, "PRODUCT":mul,
    "DIV":div, "DIVIDE":div, "DIVISION":div,
    "MODULUS":mod, "REMAINDER":mod, "MOD":mod
}

def findNumbers(l):
    numbers = []
    for i in l:
        try:
            numbers.append(float(i))
        except:
            pass
    
    return numbers


def audio():
    mixer.music.load(filename="click.mp3")
    mixer.music.play()
    
    sr = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(source= m, duration= 0.2)
            voice = sr.listen(m)
            text = sr.recognize_google(voice)
            print(text)
            text_list = text.split()
            numbers = findNumbers(text_list)
            
            for word in text_list:
                if word.upper() in operations.keys():
                    result = operations[word.upper()](numbers[0], numbers[1])
                    entry_obj.delete(0,END)
                    entry_obj.insert(0, result)
        
        except:
            pass

## ======================================================== Main Frame======================================================##

coverFrame = Frame(root, pady=2, bd=20, relief=RIDGE)
coverFrame.grid()

## ======================================================== Main Frame======================================================##

## ======================================================== Sub Frame======================================================##

coverMainFrame = Frame(coverFrame, pady=2, bd=10, bg="cadet blue", relief=RIDGE)
coverMainFrame.grid()

## ======================================================== Sub Frame======================================================##

## ======================================================== inner Frame======================================================##

MainFrame = Frame(coverMainFrame, pady=2, bd=5, relief=RIDGE)
MainFrame.grid()

## ======================================================== inner Frame======================================================##

## ======================================================== Entry screen ====================================================##
entry_var = StringVar()


entry_obj = Entry(MainFrame, width=29, textvariable=entry_var, font="Arial 16 bold", bd=20, justify=RIGHT)
entry_obj.grid(columnspan=5, padx=1, pady=1)
entry_obj.insert(0,"0")

microphone_image = Image.open("./microphone.png")
resize_microphone_image = microphone_image.resize((74,70))

mic = ImageTk.PhotoImage(resize_microphone_image)

microphone_button = Button(MainFrame, image= mic, bd=0, command=audio)
microphone_button.grid(row=0, column=5, padx=1, pady=1)

## ======================================================== Entry screen ====================================================##

## =================================================Calculator normal buttons====================================================##

CE = Button(MainFrame, text="CE", font="Arial 16 bold",height=1, width=6, bd=4,  padx=4, pady=2,  command=clear)
CE.grid(row=1, column=2, pady=1)

backSpace = Button(MainFrame, text="", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=back)
backSpace.grid(row=1, column=3, pady=1)

openBracket = Button(MainFrame, text="(", font="Arial 16 bold", bd=4, height=1, width=6, padx=4, pady=2,  command=lambda: press("("))
openBracket.grid(row=3, column=1, pady=1)

closeBracket = Button(MainFrame, text=")", font="Arial 16 bold", bd=4, height=1, width=6, padx=4, pady=2,  command=lambda: press(")"))
closeBracket.grid(row=3, column=2, pady=1)

## =================================================Calculator normal buttons====================================================##


## ================================================= Scientific Buttons =======================================================##

log = Button(MainFrame, text="log", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("log("))
log.grid(row=1, column=0, pady=1)

pi = Button(MainFrame, text="π", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(3.141529))
pi.grid(row=1, column=1, pady=1)

natural_log = Button(MainFrame, text="ln", font="Arial 16 bold", bd=4, height=1, padx=4, pady=2,  width=6,command=lambda: press("ln("))
natural_log.grid(row=2, column=0, pady=1)

factorial = Button(MainFrame, text="n!", font="Arial 16 bold italic", height=1, width=6, padx=4, pady=2,  bd=4, command=lambda: press("fac("))
factorial.grid(row=3, column=3, pady=1)

sin = Button(MainFrame, text="sin", font="Arial 16 bold", height=1, width=6, padx=4, bd=4, pady=2,  command=lambda: press("sin("))
sin.grid(row=4, column=0, pady=1)

cos = Button(MainFrame, text="cos", font="Arial 16 bold", height=1, width=6, padx=4, bd=4, pady=2,  command=lambda: press("cos("))
cos.grid(row=4, column=1, pady=1)

tan = Button(MainFrame, text="tan", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("tan("))
tan.grid(row=4, column=2, pady=1)

power = Button(MainFrame, text="pow", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("pow"))
power.grid(row=4, column=3, pady=1)

deg = Button(MainFrame, text="deg", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("deg("))
deg.grid(row=5, column=0,pady=1)

rad = Button(MainFrame, text="rad", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("rad("))
rad.grid(row=5, column=1,pady=1)

reciprocal = Button(MainFrame, text="1/x", font="Arial 16 bold", height=1, width=6,  padx=4, pady=2,  bd=4, command=lambda: press("1/("))
reciprocal.grid(row=5, column=2, pady=1)

mod = Button(MainFrame, text="mod", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("%"))
mod.grid(row=2, column=3, pady=1)

## ================================================= Scientific Buttons =======================================================##

## ================================================= Arithmetic Operations =======================================================##

square = Button(MainFrame, text="x^2", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("square("))
square.grid(row=2, column=1, pady=1)

absolute = Button(MainFrame, text="|x|", font="Arial 16 bold italic", bd=4, height=1, padx=4, pady=2,  width=6,command=lambda: press("abs("))
absolute.grid(row=2, column=2, pady=1)

sq_root = Button(MainFrame,text="√", font="Arial 16 bold", bd=4, height=1, width=6, padx=4, pady=2,  command=lambda: press("sqrt("))
sq_root.grid(row=3, column=0, pady=1)

div_btn = Button(MainFrame, text="÷", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("/"))
div_btn.grid(row=5, column=3, pady=1)

mul_btn = Button(MainFrame, text="*", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("*"))
mul_btn.grid(row=6, column=3, pady=1)

sub_btn = Button(MainFrame, text="-", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("-"))
sub_btn.grid(row=7, column=3, pady=1)

add_btn = Button(MainFrame, text="+", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("+"))
add_btn.grid(row=8, column=3, pady=1)

negate_value = Button(MainFrame, text="±", font="Arial 16 bold", height=1, width=6, padx=4, pady=2,  bd=4, command=showMinusSign)
negate_value.grid(row=9, column=0, pady=1)

## ================================================= Arithmetic Operations =======================================================##

## ========================================================= Digits ==============================================================##

seven = Button(MainFrame, text="7", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(7))                       
seven.grid(row=6, column=0, pady=1)                                                                                               

eight = Button(MainFrame, text="8", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(8))
eight.grid(row=6, column=1, pady=1)

nine = Button(MainFrame, text="9", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(9))
nine.grid(row=6, column=2, pady=1)

four = Button(MainFrame, text="4", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(4))
four.grid(row=7, column=0, pady=1)

five = Button(MainFrame, text="5", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,   command=lambda: press(5))
five.grid(row=7, column=1, pady=1)

six = Button(MainFrame, text="6", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(6))
six.grid(row=7, column=2, pady=1)

one = Button(MainFrame, text="1", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(1))
one.grid(row=8, column=0, pady=1)

two = Button(MainFrame, text="2", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(2))
two.grid(row=8, column=1, pady=1)

three = Button(MainFrame, text="3", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(3))
three.grid(row=8, column=2, pady=1)

zero = Button(MainFrame, text="0", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press(0))
zero.grid(row=9, column=1, pady=1)

dot = Button(MainFrame, text=".", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2,  command=lambda: press("."))
dot.grid(row=9, column=2, pady=1)

equals = Button(MainFrame, bg="blue", fg="white", text="=", font="Arial 16 bold", height=1, width=6, bd=4, padx=4, pady=2, command=equal)
equals.grid(row=9, column=3, pady=2)

## ========================================================= Digits ==============================================================##

root.mainloop()