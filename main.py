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

updateBtn = Button(window, text='Update', font=('Serif', 12), bg='white')
updateBtn.place(x=100, y=160)

getBtn = Button(window, text='Retrieve', font=('Serif', 12), bg='white')
getBtn.place(x=190, y=160)

deleteBtn = Button(window, text='Delete', font=('Serif', 12), bg='red')
deleteBtn.place(x=290, y=160)

resetBtn = Button(window, text='Reset', font=('Serif', 12), bg='yellow')
resetBtn.place(x=20, y=200)

window.mainloop()