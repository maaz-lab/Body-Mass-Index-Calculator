import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.geometry('550x550')
window.resizable(0, 0)
window.title("BMI")
Label(window,text="BMI CALCULATOR", font='Arial,italic,40',).pack(pady=5)
Label(window,text="BMI Categories\nUnderweight = < 18.5 (Less than 18.5)"
                  "\nNormalweight = 18.5 - 24.9\nOverweight = 25 - 29.9"
                  "\nObesity = BMI of 30 or Greater").pack(pady=10)

Label(window,text="Height in ft").pack()

height_ft = Entry(window, width=15, justify='center',borderwidth=3)
height_ft.pack(pady=7)

Label(window,text="Weight in Kilo").pack()
en1 = Entry(window,width=15,justify='center',borderwidth=3)
en1.pack(pady=7)

entry = Entry(window,width=10,justify='center',borderwidth=3)
entry1 = Entry(window,width=20,justify='center',borderwidth=3)
def clear():
    en1.delete(0,END)
    height_ft.delete(0,END)
    entry.delete(0,END)
    entry1.delete(0,END)

def myclick():
    height_metre = float(height_ft.get()) * 0.3048
    orig = pow(height_metre, 2)
    Bmi = float(en1.get()) / orig
    entry.insert(0,round(Bmi,1))
    if Bmi < 18.5:
        text = "You are Underweight"
        entry1.insert(0,text)
        entry1.config(bg="Light Blue")

    if Bmi >= 18.5 and Bmi <= 24.9:
        text = "Your weight is Normal"
        entry1.insert(0, text)
        entry1.config(bg="Light Green")

    if Bmi > 25 and Bmi <= 29.9:
        text = "You are Overweight"
        entry1.insert(0, text)
        entry1.config(bg="Red",fg="White")

    if Bmi > 30:
        text = "You are Obseity"
        entry1.insert(0, text)
        entry1.config(bg="Pink",fg="White")

def membership():
    window1 = tkinter.Tk()
    window1.geometry('500x500')
    window1.resizable(0,0)
    window1.title("Membership Detail")

    def Basic():
        window1.destroy()
        messagebox.showinfo("Membership Activated","Congratulation Your Basic Package is Activated")

    def Regular():
        window1.destroy()
        messagebox.showinfo("Membership Activated", "Congratulation Your Regular Package is Activated")

    def Premium():
        window1.destroy()
        messagebox.showinfo("Membership Activated", "Congratulation Your Premium Package is Activated")

    label = Label(window1,text="MEMBERSHIP DETAILS",font='Arial,50').pack(pady=5)
    Label(window1,text="BASIC\nIn Basic Package you check your BMI on Weekly Basis "
          "\nmeans you can Check your BMI only three times in a Week").pack()
    Basic_Package = Button(window1,text="BASIC",command=Basic,width=10).pack(pady=4)
    Label(window1,text="\nREGULAR\nIn Regular Package you check your BMI on same Weekly Basis "
          "\nbut you can Check your BMI Five times i a Week").pack()
    Regular_Package = Button(window1, text="REGULAR",command=Regular,width=10).pack(pady=4)
    Label(window1,text="\nPREMIUM\nIn Premium Package you check your BMI on daily Basis "
          "\nmeans you can Check your BMI on a daily basis in a Week").pack()
    Premium_Package = Button(window1, text="PREMIUM",command=Premium,width=10).pack(pady=4)

    def exit():
        window1.destroy()

    Exit = Button(window1,text="Exit",width=10,command=exit,bg="Light Blue",).pack(pady=40)
    window1.mainloop()

mybutton = Button(window, text="Compute", command=myclick,width=10,borderwidth=3,bg="Light Green").pack(pady=6,)
clearall = Button(window,text="Clear All",command=clear,width=10,borderwidth=3,bg="Light Gray").pack()
Bt = Button(window,text="Exit",command=window.destroy,bg="Light Blue",width=10,borderwidth=3).pack(pady=4)
Label(window,text="Your BMI: ").pack(pady=10)
entry.pack()
entry1.pack()
Button(window,text="View Membership",command=membership,bg="Pink").pack(pady=10)
window.mainloop()
