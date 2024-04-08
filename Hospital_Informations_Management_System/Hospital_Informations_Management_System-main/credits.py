from tkinter import *

def credits_press(window, fulwidth, fulheight):
    credit_subwin = Toplevel(window)
    credit_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    credit_subwin.iconphoto(False, icon)
    credit_subwin.title("Credits")
    Frame(credit_subwin, bg='deep sky blue').place(x=0, y=0 ,width=fulwidth, height=fulheight)

    Label(credit_subwin, bg='deep sky blue', fg='white', text='BI11-168 _ Jaya Singh', anchor='w', font=("Ariel", 20, 'bold')).place(x=100, y=100, width=fulwidth-200, height = 50)
    Label(credit_subwin, bg='deep sky blue', fg='white', text='BI11-205 _ Kriti Mishra', anchor='w', font=("Ariel", 20, 'bold')).place(x=100, y=170, width=fulwidth-200, height = 50)
    Label(credit_subwin, bg='deep sky blue', fg='white', text='BI11-205 _ Ritima Sharma', anchor='w', font=("Ariel", 20, 'bold')).place(x=100, y=170, width=fulwidth-200, height = 50)
    Label(credit_subwin, bg='deep sky blue', fg='white', text='BI11-205 _ Sarika Rajput', anchor='w', font=("Ariel", 20, 'bold')).place(x=100, y=170, width=fulwidth-200, height = 50)
    Label(credit_subwin, bg='deep sky blue', fg='red', text='GROUP 5', font=("Ariel", 30, 'bold')).place(x=fulwidth/4*3-100, y=fulheight/2-50, width=200, height = 70)



    