from tkinter import*
from tkinter import font as tkFont
base = Tk(className='Python Examples - Window Color')
base.title("Calculator")
base.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/ne.ico')
helv36 = tkFont.Font(family='Helvetica', size=15)
e = Entry (base , width=50 , fg = "red",  bg = 'black', borderwidth=5 )
e.grid (row=0 , column=0 , padx=10 , pady=10 , columnspan=4)
base['bg']='black'

def myclick(number):
    recent = e.get()
    e.delete(0, END)
    e.insert(0, str(recent) + str(number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0 , END)



def button_clear():
    e.delete(0,END)




def button_equal():
    second_number = e.get()
    e.delete(0,END)


    if math == "addition" :
        e.insert(0, f_num + float(second_number))

    elif math == "subtraction" :
        e.insert(0, f_num - float(second_number))

    elif math == "multiplication" :
        e.insert(0, f_num * float(second_number))

    elif math == "division" :
        e.insert(0, f_num / float(second_number))



def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def  button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_square():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = float(first_number)
    e.delete(0, END)



button_1 = Button(base , text="1" , padx= 40 ,fg= "black" , bg = 'white' , pady = 20 ,font = helv36, command = lambda : myclick(1))
button_2 = Button(base , text = "2" , padx= 40 , fg= "black" , bg = 'white' ,pady = 20 ,font = helv36, command = lambda : myclick(2))
button_3 = Button(base , text = "3" , padx= 41 , fg= "black" , bg = 'white' ,pady = 20 ,font = helv36, command = lambda : myclick(3))
button_4 = Button(base , text = "4" , padx= 40 ,fg= "black" , bg = 'white' , pady = 20 ,font = helv36, command = lambda : myclick(4))
button_5 = Button(base , text = "5" , padx= 40 ,fg= "black" , bg = 'white' , pady = 20 , font = helv36,command = lambda : myclick(5))
button_6 = Button(base , text = "6" , padx= 41 ,fg= "black" , bg = 'white' , pady = 20 ,font = helv36, command = lambda : myclick(6))
button_7 = Button(base , text = "7" , padx= 40 ,fg= "black" , bg = 'white' , pady = 20 ,font = helv36, command = lambda : myclick(7))
button_8 = Button(base , text = "8" , padx= 40 ,fg= "black" , bg = 'white' , pady = 20 ,font = helv36, command = lambda : myclick(8))
button_9 = Button(base , text = "9" , padx= 41 ,fg= "black" , bg = 'white' , pady = 20 ,font = helv36, command = lambda : myclick(9))
button_0 = Button(base , text = "0" , padx= 40 , fg= "black" , bg = 'white' ,pady = 20 , font = helv36, command = lambda : myclick(0))
button_add = Button(base , text = "+" , padx= 60,fg= "white" , bg = 'black' , pady = 20 , font = helv36,command = button_add)
button_clear = Button(base , text = "clear" ,fg= "white" , bg = 'black' , padx= 43, pady = 20 , font = helv36,command = button_clear)
button_equal = Button(base , text = "=" ,fg= "white" , bg = 'black' , padx= 221, pady = 20 ,font = helv36, command = button_equal)
button_subtract = Button(base , text = "-" ,fg= "white" , bg = 'black' , padx= 62, pady = 20 ,font = helv36, command = button_subtract)
button_divide = Button(base , text = "/" ,fg= "white" , bg = 'black' , padx= 43, pady = 20 ,font = helv36, command = button_divide)
button_multiply = Button(base , text = "*" , fg= "white" , bg = 'black' ,padx= 43, pady = 20 ,font = helv36, command = button_multiply)
button_decimal = Button (base , text = "." , fg = "white" , bg = "black" ,padx = 63 , pady = 20 ,font = helv36 , command = lambda : myclick('.'))

button_1.grid(row= 1 ,column = 0)
button_2.grid(row= 1,column = 1)
button_3.grid(row= 1,column =2 )

button_4.grid(row= 2,column =0 )
button_5.grid(row=2 ,column = 1)
button_6.grid(row= 2,column = 2)

button_7.grid(row=3,column = 0)
button_8.grid(row=3 ,column = 1)
button_9.grid(row=3 ,column = 2)

button_0.grid(row= 4,column = 0)
button_add.grid(row = 1, column =3 )
button_clear.grid(row = 4, column =3 )
button_equal.grid(row = 5 , column =0, columnspan = 4)
button_subtract.grid(row = 3, column =3 )
button_divide.grid(row = 4, column =1 )
button_multiply.grid(row = 4, column =2)
button_decimal.grid(row = 2, column =3)




base.mainloop()