
#Python program to create a simple GUI project
#Calculator using Tkinter

#import modules from tkinter
import tkinter
from tkinter import *


#Create a main window using Tkinter  variable root
cal =Tk()

#Set the background color for GUI window
cal.configure(bg="#17161b")

#Set the title to GUI window
cal.title("simple calculator")

#set the configuration to  GUI window
cal.geometry("570x600+100+200")

#Create a global variable
expression =" "

#Function to clear the input field text
def clear():
    global expression
    expression =" "
    result.config(text=expression)

#FUnction to update the expression
def show(value):
    global expression
    expression+= value
    result.config(text=expression)

#FUnction to calculate the expression  present in text field box
def calculate():
    global expression
    res =" "
    if expression !="":
        try:
            res=eval(expression)
        except:
            res="error"
            expression=" "
    result.config(text=res)

#Create a text entry field box using label function
result=Label(cal,width=25,height=2,text="",font=("arial",30))

#Pack is used for placing the text box
result.pack()


#Create  Buttons and place at a particular positions 
#use command to update expression
Button(cal,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(cal,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
Button(cal,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
Button(cal,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)

Button(cal,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
Button(cal,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
Button(cal,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
Button(cal,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("-")).place(x=430,y=200)

Button(cal,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
Button(cal,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
Button(cal,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
Button(cal,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("+")).place(x=430,y=300)

Button(cal,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
Button(cal,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
Button(cal,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
Button(cal,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show("0")).place(x=10,y=500)

Button(cal,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#2a2d36",command=lambda: show(".")).place(x=290,y=500)
Button(cal,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#3697f5",command=lambda: calculate()).place(x=430,y=400)


#start the main loop
cal.mainloop()







