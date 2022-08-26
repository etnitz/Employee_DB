from tkinter import *

window = Tk()
window.geometry('600x270')
window.title('Employee Database App')

empId = Label(window, text='Employee ID', font=('Serif', 12))
empId.place(x=20, y=30)

window.mainloop()