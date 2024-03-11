'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from ctypes import alignment
from operator import truediv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
from turtle import left

class Employee:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        employee_page = Tk()
        employee_page.title('Employee')
        employee_page.geometry("800x800")
        employee_page.configure(bg = "#bed2fa")

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        employee_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        employee_page_header = Label(employee_page, text = "Employees", font=font_specifications_heading, fg="black", bg="#bed2fa")
        employee_page_header.place(x = 400, y = 20)

        def go_to_add_employee():
            from AddEmployee import Add_Employee
            employee_page.destroy()
            Add_Employee().main()

        def go_to_edit_employee():
            from EditEmployee import Edit_Employee
            employee_page.destroy()
            Edit_Employee().main()

        # Creating buttons and arranging them on the screen
        add_employee_btn = Button(employee_page, text = "Add New Employee +", font = font_specifications_regular, width = 18, command = go_to_add_employee)
        add_employee_btn.place(x = 40, y = 120, width = 250)
        edit_employee_btn = Button(employee_page, text = "Edit Employee Details", font = font_specifications_regular, width = 18, command = go_to_edit_employee)
        edit_employee_btn.place(x = 700, y = 120, width = 250)

        # Table

        # Setting the style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight = 30)

        # Using the treeview widget
        employee_trv = ttk.Treeview(employee_page, selectmode ='browse', height = 7)

        # Placing the table
        employee_trv.place(x = 40, y = 200)

        # Number of columns
        employee_trv["columns"] = ("1", "2", "3","4", "5", "6", "7")
        
        # Defining the headings
        employee_trv['show'] = 'headings'
        
        # Defining the width of columns and their alignment 
        employee_trv.column("1", width = 50, anchor ='c')
        employee_trv.column("2", width = 165, anchor ='c')
        employee_trv.column("3", width = 110, anchor ='c')
        employee_trv.column("4", width = 130, anchor ='c')
        employee_trv.column("5", width = 210, anchor ='c')
        employee_trv.column("6", width = 120, anchor ='c')
        employee_trv.column("7", width = 125, anchor ='c')
        
        # Adding headings to columns
        employee_trv.heading("1", text = "ID")
        employee_trv.heading("2", text = "Employee Name")
        employee_trv.heading("3", text = "Date of birth")
        employee_trv.heading("4", text = "Mobile Number") 
        employee_trv.heading("5", text = "Address")  
        employee_trv.heading("6", text = "Job Grade")  
        employee_trv.heading("7", text = "Salary (8hrs)")   

        # Getting data from the database 'products' table 
        r_set = cursor.execute('''SELECT * from employees LIMIT 0,10''')
        for dt in r_set: 
            employee_trv.insert("", 'end', iid = dt[0], text = dt[0], values = (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        def back_to_menu():
            from Menu import Menu
            employee_page.destroy()
            Menu().main()

        # Creating an exit button
        exit_button = Button(employee_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 850, y = 15)

        # Creating a back-to-menu button
        back_to_menu_button = Button(employee_page, text = "Back to menu", font = font_specifications_regular, command = back_to_menu)
        back_to_menu_button.place(x = 830, y = 510)

        employee_page.mainloop()