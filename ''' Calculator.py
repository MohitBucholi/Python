''' Calculator 
    using python
    '''
# import linbrary for GUI
from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        expression = total
        equation.set(total)

    except:
        equation.set("error")
        expression =""
    
def percentage_():
    global expression
    expression = expression +'*' +str(0.01)
    expression = str(eval(expression))
    equation.set(expression)

def clear():
    global expression
    expression=""
    equation.set(expression)

def backslash():
    try:
        global expression
        expression = expression[:-1]
        equation.set(expression)
    except:
        expression = ""
        equation.set(expression)

# CREATE GUI 

if __name__ == "__main__":

    w = Tk()
    w.configure(background="black")
    w.title("Mohit Bucholi")
    w.geometry('360x200')

    equation =StringVar()

    equation_display = Entry(w, textvariable=equation)
    equation_display.grid(columnspan=4,ipadx=70)

    equation.set("Enter Your Equation")

    b1 = Button(w, text=' 1 ', fg='black', bg='brown', command=lambda: press(1), height=1, width=7)
    b1.grid(row=4,column=1)
    b2 = Button(w,text='2',fg ="black", bg= 'brown', command=lambda: press(2),height =1,width=7)
    b2.grid(row=4,column=2)
    b3 = Button(w,text='3',fg ="black", bg= 'brown', command=lambda: press(3),height =1,width=7)
    b3.grid(row=4,column=3)
    b4 = Button(w,text='4',fg ="black", bg= 'brown', command=lambda: press(4),height =1,width=7)
    b4.grid(row=3,column=1)
    b5 = Button(w,text='5',fg ="black", bg= 'brown', command=lambda: press(5),height =1,width=7)
    b5.grid(row=3,column=2)
    b6 = Button(w,text='6',fg ="black", bg= 'brown', command=lambda: press(6),height =1,width=7)
    b6.grid(row=3,column=3)
    b7 = Button(w,text='7',fg ="black", bg= 'brown', command=lambda: press(7),height =1,width=7)
    b7.grid(row=2,column=1)
    b8 = Button(w,text='8',fg ="black", bg= 'brown', command=lambda: press(8),height =1,width=7)
    b8.grid(row=2,column=2)
    b9 = Button(w,text='9',fg ="black", bg= 'brown', command=lambda: press(9),height =1,width=7)
    b9.grid(row=2,column=3)
    b0 = Button(w,text='0',fg ="black", bg= 'brown', command=lambda: press(0),height =1,width=7)
    b0.grid(row=5,column=2)
    decimal = Button(w,text='.',fg ="black", bg= 'brown', command=lambda: press('.'),height =1,width=7)
    decimal.grid(row=5,column=3)
    add = Button(w,text="+",fg='black',bg='gray', command=lambda: press('+'),height=1,width=7)
    add.grid(row=4 ,column=5)
    sub = Button(w,text="-",fg='black',bg='gray', command=lambda: press('-'),height=1,width=7)
    sub.grid(row=3 ,column=5)
    mult = Button(w,text="X",fg='black',bg='gray', command=lambda: press('*'),height=1,width=7)
    mult.grid(row= 2,column=5)
    divide = Button(w,text="/",fg='black',bg='gray', command=lambda: press("/"),height=1,width=7)
    divide.grid(row=1 ,column=5)
    percentage = Button(w,text="%",fg='black',bg='gray', command=lambda: percentage_(),height=1,width=7)
    percentage.grid(row=1 ,column=3)
    clear_ = Button(w,text="C",fg='black',bg='gray', command=lambda: clear(),height=1,width=7)
    clear_.grid(row=1 ,column=1)
    equal_ = Button(w,text="=",fg='black',bg='gray', command=lambda: equal(),height=1,width=7)
    equal_.grid(row=5 ,column=5)
    back = Button(w,text="<-",fg='black',bg='gray', command=lambda: backslash(),height=1,width=7)
    back.grid(row= 1,column=2)
    #diff_calcu = Button(w,text="<>",fg='black',bg='gray', command=lambda: backslash(),height=1,width=7)
    #diff_calcu.grid(row= 5,column=1)
w.mainloop()