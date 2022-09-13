from email import message
from tkinter import *
from tkinter import messagebox
import mysql.connector

def insertData():
    
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if id == '' or name == '' or dept == '':
        messagebox.showwarning('Cannot Insert','All fields required!')
    else:
        myDb = mysql.connector.connect(host='localhost', user='root', password='password', database='employee')
        myCur = myDb.cursor()
        insertQuery = """INSERT INTO staff(staff_id, name, department) VALUES(%s, %s, %s)"""
        record = (id, name, dept)
        myCur.execute(insertQuery, record)
        myDb.commit()

        enterId.delete(0, 'end')
        enterName.delete(0, 'end')
        enterDept.delete(0, 'end')

        messagebox.showinfo('Enter Status','Data entered sucessfully!')
        myDb.close()

def updateData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if id == '' or name == '' or dept == '':
        messagebox.showwarning('Cannot update', 'All fields required!')
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='employee')
        myCur = myDB.cursor()
        updateQuery = "UPDATE staff SET name = %s, department = %s WHERE staff_id = %s"
        record = (name, dept, id)
        myCur.execute(updateQuery, record)
        myDB.commit()

        enterId.delete(0, 'end')
        enterName.delete(0, 'end')
        enterDept.delete(0, 'end')

        messagebox.showinfo('Update Status','Data updated sucessfully!')
        myDB.close()

def getData():
    id = enterId.get()
    if id == '':
        messagebox.showwarning('Fetch Status', "Please provide the employee ID to fetch the data")
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='employee')
        myCur = myDB.cursor()
        getQuery = "SELECT * FROM staff WHERE staff_id = %s"
        record = (id)
        myCur.execute(getQuery, record)
        rows = myCur.fetchall()
        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])
        myDB.close()

def deleteData():
    id = enterId.get()
    if id == '':
        messagebox.showwarning('Cannot Delete', 'Please provide employee ID to delete the data')
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='employee')
        myCur = myDB.cursor()
        myCur.execute("DELETE FROM staff WHERE staff_id = 'enterId.get()'")
        myDB.commit()

        enterId.delete(0, 'end')
        enterName.delete(0, 'end')
        enterDept.delete(0, 'end')

        messagebox.showinfo("Delete Status", 'Data deleted successfully')
        myDB.close()

window = Tk()
window.geometry('650x270')
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

insertBtn = Button(window, text='Insert', font=('Serif', 12), bg='white', command=insertData)
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text='Update', font=('Serif', 12), bg='white', command=updateData)
updateBtn.place(x=100, y=160)

getBtn = Button(window, text='Retrieve', font=('Serif', 12), bg='white', command=getData)
getBtn.place(x=190, y=160)

deleteBtn = Button(window, text='Delete', font=('Serif', 12), bg='red', command=deleteData)
deleteBtn.place(x=290, y=160)

resetBtn = Button(window, text='Reset', font=('Serif', 12), bg='yellow')
resetBtn.place(x=20, y=200)

showData = Listbox(window)
showData.place(x=450, y=30)

window.mainloop()

