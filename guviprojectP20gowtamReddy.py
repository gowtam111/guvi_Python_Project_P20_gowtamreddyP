#Project for
#i) GUI to store address into database
#ii) A second GUI to retrieve data from database


import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='employees'
)

my_cursor = mydb.cursor()
my_cursor = mydb.cursor(buffered=True)

try:
    my_cursor.execute("use master_students")
except:
    my_cursor.execute("CREATE DATABASE master_students")
    my_cursor.execute("use master_students")
try:
    my_cursor.execute("desc students_address")
except:
    my_cursor.execute(
        "create table students_address (name VARCHAR(50), gender char(10), city VARCHAR(20), age varchar(10), email VARCHAR("
        "50), pincode VARCHAR(10))")


def submit_address_details():
    my_cursor.execute(
        f"insert into students_address (name, gender, city, age, email, pincode) values ('{entry1.get()}','{entry2.get()}','{entry3.get()}','{entry4.get()}','{entry5.get()}','{entry6.get()}')")
    mydb.commit()

def reset_details():
    user = entry1.get()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


def search_details():
    my_cursor.execute(f"select * from students_address where name='{entry7.get()}'")
    row = my_cursor.fetchone()
    if row == None:
        messagebox.showwarning("Warning!!", "Name not found in the address list")
    else:
        my_cursor.execute(f"select * from students_address where name='{entry7.get()}'")
        i = 11
        for student in my_cursor:
            for j in range(len(student)):
                e = Entry(box1, width=25, fg='black')
                e.pack(side="bottom")
                e.insert(END, student[j])
        i = i + 1

def clear_details():
    user = entry7.get()
    entry7.delete(0, END)

box = tkinter.Tk()
box.title('Guvi Address Management for insert')
font1 = ('Calibri', 20)
box.geometry("+500+100")

box1 = tkinter.Tk()
box1.title('Guvi Fetch Student address')
box1.geometry("+500+550")

labelmain = Label(master=box, text='Guvi Students Address Insert', font=font1, fg='#050000',
                  background='Grey',
                  width='50', height='3')
label1 = Label(master=box, text='name:', font=font1, fg='#050000', background='LightSalmon', width='10')
label2 = Label(master=box, text='gender:', font=font1, fg='#050000', background='LightSalmon', width='10')
label3 = Label(master=box, text='city:', font=font1, fg='#050000', background='LightSalmon', width='10')
label4 = Label(master=box, text='Age:', font=font1, fg='#050000', background='LightSalmon', width='10')
label5 = Label(master=box, text='email:', font=font1, fg='#050000', background='LightSalmon', width='10')
label6 = Label(master=box, text='pincode:', font=font1, fg='#050000', background='LightSalmon', width='10')
label7 = Label(master=box1, text='name:', font=font1, fg='#050000', background='LightSalmon', width='10')
entry1 = Entry(master=box, font=font1, fg='#050000', background='White', width='10')
entry2 = Entry(master=box, font=font1, fg='#050000', background='White', width='10')
entry3 = Entry(master=box, font=font1, fg='#050000', background='White', width='10')
entry4 = Entry(master=box, font=font1, fg='#050000', background='White', width='10')
entry5 = Entry(master=box, font=font1, fg='#050000', background='White', width='10')
entry6 = Entry(master=box, font=font1, fg='#050000', background='White', width='10')
entry7 = Entry(master=box1, font=font1, fg='#050000', background='White', width='10')
button1 = Button(master=box, text='Submit', font=font1, fg='#050000', background='White', width='8', height='1',
                 command=submit_address_details)
button2 = Button(master=box, text='Reset', font=font1, fg='#050000', background='White', width='8', height='1',
                 command=reset_details)
labelfetch = Label(master=box1, text='Guvi Students Address Fetch', font=font1, fg='#050000',background='Grey',
                  width='50', height='3')
button3 = Button(master=box1, text='Fetch', font=font1, fg='#050000', background='White', width='8', height='1',
                 command=search_details)
button4 = Button(master=box1, text='Clear', font=font1, fg='#050000', background='White', width='8', height='1',
                 command=clear_details)
labelmain.grid(column=0, row=0, columnspan=3)
label1.grid(row=1, column=1)
label2.grid(row=2, column=1)
label3.grid(row=3, column=1)
label4.grid(row=4, column=1)
label5.grid(row=5, column=1)
label6.grid(row=6, column=1)
entry1.grid(row=1, column=2)
entry2.grid(row=2, column=2)
entry3.grid(row=3, column=2)
entry4.grid(row=4, column=2)
entry5.grid(row=5, column=2)
entry6.grid(row=6, column=2)
button1.grid(row=7, column=1)
button2.grid(row=7, column=2)
# labelfetch.pack(column=0, row=8, columnspan=3)
# label7.pack(row=9, column=1)
# entry7.pack(row=9, column=2)
# button3.pack(row=10, column=1)
# button4.pack(row=10, column=2)
labelfetch.pack()
label7.pack(side="left")
entry7.pack(side="left")
button3.pack(side="left")
button4.pack(side="left")
box.mainloop()
box1.mainloop()
