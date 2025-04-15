'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import sqlite3

class Add_Employee:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        add_employee_page = Tk()
        add_employee_page.title('Add Employee')
        add_employee_page.geometry("800x800")
        add_employee_page.configure(bg="#bed2fa")

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        add_employee_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        add_employee_page_header = Label(add_employee_page, text = "Add Employee", font = font_specifications_heading, fg = "black", bg = "#bed2fa")
        add_employee_page_header.place(x = 360, y = 15)

        # Adding entry boxes for company name and est. delivery date

        employee_id = Entry(add_employee_page, width = 35, font = font_specifications_regular)
        employee_id.insert(0, "Employee ID")
        employee_id.place(x = 50, y = 95)

        employee_name = Entry(add_employee_page, width = 35, font = font_specifications_regular)
        employee_name.insert(0, "Employee Name")
        employee_name.place(x = 480, y = 95)

        employee_dob = Entry(add_employee_page, width = 35, font = font_specifications_regular)
        employee_dob.insert(0, "YYYY-MM-DD")
        employee_dob.place(x = 50, y = 140)

        employee_mobile_no = Entry(add_employee_page, width = 35, font = font_specifications_regular)
        employee_mobile_no.insert(0, "Mobile No.")
        employee_mobile_no.place(x = 480, y = 140)

        employee_address = Entry(add_employee_page, width = 74, font = font_specifications_regular)
        employee_address.insert(0, "Address")
        employee_address.place(x = 50, y = 185)

        employee_job_grade = Entry(add_employee_page, width = 35, font = font_specifications_regular)
        employee_job_grade.insert(0, "Job Grade")
        employee_job_grade.place(x = 50, y = 230)

        employee_salary = Entry(add_employee_page, width = 35, font = font_specifications_regular)
        employee_salary.insert(0, "Salary")
        employee_salary.place(x = 480, y = 230)

        # Adding to the database
        def add_employee():
            
            # Grab the selected employee
            selected = employee_trv.focus()
            
            # Checking if name has any number
            name_check = employee_name.get() != '' and all(c.isalpha() or c.isspace() for c in employee_name.get())
            # Checking if mobile number has any alphabet
            number_check = employee_mobile_no.get().isnumeric()
            # Checking if salary has any alphabet
            salary_check = employee_salary.get().isnumeric()
            
            if name_check == False or number_check == False or salary_check == False:
                if name_check == False:
                    messagebox.showerror("showerror", "Invalid name!")
                else:
                    if number_check == False:
                        messagebox.showerror("showerror", "Invalid mobile number!")
                    else:
                        messagebox.showerror("showerror", "Invalid salary!")
            else:

                # i = len(employee_trv.get_children())
                # employee_trv.insert("", 'end', iid = i+1, values = (employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary))
                # Connecting database
                conn = sqlite3.connect("data.db")
                # Creating a cursor
                c = conn.cursor()

                # Add new product
                c.execute("INSERT INTO employees VALUES (:employee_id, :employee_name, :employee_dob, :employee_mobile_no, :employee_address, :employee_job_grade, :employee_salary)",
                {
                    'employee_id': employee_id.get(),
                    'employee_name': employee_name.get(),
                    'employee_dob': employee_dob.get(),
                    'employee_mobile_no': employee_mobile_no.get(),
                    'employee_address': employee_address.get(),
                    'employee_job_grade': employee_job_grade.get(),
                    'employee_salary': employee_salary.get(),
                })

                messagebox.showinfo("showinfo", "Employee added successfully!")

                conn.commit()
                conn.close()

                employee_trv.insert(parent = '', index = 'end', text = "", values = (employee_id.get(), employee_name.get(), employee_dob.get(), employee_mobile_no.get(), employee_address.get(), employee_job_grade.get(), employee_salary.get()))
                
                employee_id.delete(0, END)
                employee_name.delete(0, END)
                employee_dob.delete(0, END)
                employee_mobile_no.delete(0, END)
                employee_address.delete(0, END)
                employee_job_grade.delete(0, END)
                employee_salary.delete(0, END)

        # Creating buttons
        add_employee_button = Button(add_employee_page, text = "Add Employee", font = font_specifications_regular, command = add_employee)
        add_employee_button.place(x = 50, y = 280)

        # Table

        # Setting the style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight = 28)

        # Change selected color
        # style.map('Treeview', background[('selected','green')])

        # Using the treeview widget
        employee_trv = ttk.Treeview(add_employee_page, selectmode ='browse', height = 5)

        # Placing the table
        employee_trv.place(x = 50, y = 330)

        # Number of columns
        employee_trv["columns"] = ("1", "2", "3","4", "5", "6", "7")
        
        # Defining the headings
        employee_trv['show'] = 'headings'
        
        # Defining the width of columns and their alignment 
        employee_trv.column("1", width = 50, anchor ='c')
        employee_trv.column("2", width = 155, anchor ='c')
        employee_trv.column("3", width = 100, anchor ='c')
        employee_trv.column("4", width = 130, anchor ='c')
        employee_trv.column("5", width = 180, anchor ='c')
        employee_trv.column("6", width = 110, anchor ='c')
        employee_trv.column("7", width = 100, anchor ='c')
        
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
            employee_trv.insert("", 'end',iid = dt[0], text = dt[0], values = (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        def back_to_menu():
            from Menu import Menu
            add_employee_page.destroy()
            Menu().main()

        # Creating an exit button
        exit_button = Button(add_employee_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 850, y = 15)

        # Creating a back-to-menu button
        back_to_menu_button = Button(add_employee_page, text = "Back to menu", font = font_specifications_regular, command = back_to_menu)
        back_to_menu_button.place(x = 830, y = 510)

        add_employee_page.mainloop()