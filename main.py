from tkinter import *

window = Tk()
window.geometry('700x270')
window.title('Employee Database App')

empId = Label(window, text='Employee ID', font=('Serif', 12))
empId.place(x=20, y=30)

empName = Label(window, text='Employee Name', font=('Serif', 12))
empName.place(x=20, y=60)

empDept = Label(window, text='Employee Department', font=('Serif', 12))
empDept.place(x=20, y=90)

enterId = Entry(window)
enterId.place(x=230, y=30)

enterName = Entry(window)
enterName.place(x=230, y=60)

enterDept = Entry(window)
enterDept.place(x=230, y=90)

insertBtn = Button(window, text='Insert', font=('Serif', 12), bg='white')
insertBtn.place(x=20, y=160)

window.mainloop()