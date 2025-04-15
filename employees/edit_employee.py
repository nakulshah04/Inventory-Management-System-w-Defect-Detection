'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import sqlite3

class Edit_Employee:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        edit_employee_page = Tk()
        edit_employee_page.title('Edit Employee')
        edit_employee_page.geometry("800x800")
        edit_employee_page.configure(bg = "#bed2fa")

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        edit_employee_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        edit_employee_page_header = Label(edit_employee_page, text = "Edit Employee", font = font_specifications_heading, fg = "black", bg = "#bed2fa")
        edit_employee_page_header.place(x = 360, y = 15)

        # Adding entry boxes

        employee_id = Entry(edit_employee_page, width = 35, font = font_specifications_regular)
        employee_id.insert(0, "Employee ID")
        employee_id.place(x = 50, y = 95)

        employee_name = Entry(edit_employee_page, width = 35, font = font_specifications_regular)
        employee_name.insert(0, "Employee Name")
        employee_name.place(x = 480, y = 95)

        employee_dob = Entry(edit_employee_page, width = 35, font = font_specifications_regular)
        employee_dob.insert(0, "Date Of Birth (YYYY-MM-DD)")
        employee_dob.place(x = 50, y = 137)

        employee_mobile_no = Entry(edit_employee_page, width = 35, font = font_specifications_regular)
        employee_mobile_no.insert(0, "Mobile No.")
        employee_mobile_no.place(x = 480, y = 137)

        employee_address = Entry(edit_employee_page, width = 74, font = font_specifications_regular)
        employee_address.insert(0, "Address")
        employee_address.place(x = 50, y = 179)

        employee_job_grade = Entry(edit_employee_page, width = 35, font = font_specifications_regular)
        employee_job_grade.insert(0, "Job Grade")
        employee_job_grade.place(x = 50, y = 221)

        employee_salary = Entry(edit_employee_page, width = 35, font = font_specifications_regular)
        employee_salary.insert(0, "Salary")
        employee_salary.place(x = 480, y = 221)

        def edit_employee():
            
            # Grab the selected employee
            selected = employee_trv.focus()

            # Getting the employee name
            name = employee_name
            
            # Checking if name has any number
            name_check = name.get() != '' and all(c.isalpha() or c.isspace() for c in name.get())
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
                # Update record
                employee_trv.item(selected, text = "", values = (employee_id.get(), employee_name.get(), employee_dob.get(), employee_mobile_no.get(), employee_address.get(), employee_job_grade.get(), employee_salary.get(),))
                
                # Connecting to database
                conn = sqlite3.connect('data.db')
                # Create a cursor instance
                c = conn.cursor()
                
                # Query
                c.execute("""UPDATE employees SET
                
                    employee_id = :employee_id,
                    employee_name = :employee_name,
                    employee_dob = :employee_dob,
                    employee_mobile_no = :employee_mobile_no,
                    employee_address = :employee_address,
                    employee_job_grade = :employee_job_grade,
                    employee_salary = :employee_salary
                    
                    WHERE employee_id = :employee_id""",
                    {
                        'employee_id': employee_id.get(),
                        'employee_name': employee_name.get(),
                        'employee_dob': employee_dob.get(),
                        'employee_mobile_no': employee_mobile_no.get(),
                        'employee_address': employee_address.get(),
                        'employee_job_grade': employee_job_grade.get(),
                        'employee_salary': employee_salary.get(),
                    })
                
                # Commit changes
                conn.commit()
                # Close connection
                conn.close()

                messagebox.showinfo("showinfo", "Employee saved successfully!")

                # Clear entry boxes
                employee_id.delete(0, END)
                employee_name.delete(0, END)
                employee_dob.delete(0, END)
                employee_mobile_no.delete(0, END)
                employee_address.delete(0, END)
                employee_job_grade.delete(0, END)
                employee_salary.delete(0, END)

        # Removing an employee
        def delete_employee():
            
            answer = messagebox.askyesno("askyesno", "Are you sure you want to delete the employee?")
            if answer:
                x = employee_trv.selection()
                employee_trv.delete(x)
                # Connecting to database
                conn = sqlite3.connect('data.db')
                # Creating a cursor instance
                c = conn.cursor()
                # Deleting from database
                c.execute("DELETE FROM employees WHERE employee_id=" + employee_id.get())
                
                messagebox.showinfo("showinfo", "Employee deleted successfully!")

                # Clearing entry boxes
                employee_id.delete(0, END)
                employee_name.delete(0, END)
                employee_dob.delete(0, END)
                employee_mobile_no.delete(0, END)
                employee_address.delete(0, END)
                employee_job_grade.delete(0, END)
                employee_salary.delete(0, END)
                # Commit changes
                conn.commit()
                # Close connection
                conn.close()
            else:
                pass

        def employee_selected():
            # Grabbinf the employee details
            employee_selected = employee_trv.focus()
            employee_details = employee_trv.item(employee_selected, 'values')
            # Clearing values
            employee_id.delete(0, END)
            employee_name.delete(0, END)
            employee_dob.delete(0, END)
            employee_mobile_no.delete(0, END)
            employee_address.delete(0, END)
            employee_job_grade.delete(0, END)
            employee_salary.delete(0, END)
            # Filling in values
            employee_id.insert(0, employee_details[0])
            employee_name.insert(0, employee_details[1])
            employee_dob.insert(0, employee_details[2])
            employee_mobile_no.insert(0, employee_details[3])
            employee_address.insert(0, employee_details[4])
            employee_job_grade.insert(0, employee_details[5])
            employee_salary.insert(0, employee_details[6])

        # Select employee
        select_employee = Button(edit_employee_page, text = "Select employee", width = 12, font = font_specifications_regular, command = employee_selected)
        select_employee.place(x = 50, y = 495, width = 200)

        # Creating a button to save the edited product to the list
        save_changes_btn = Button(edit_employee_page, text = "Save Employee", font = font_specifications_regular, command = edit_employee)
        save_changes_btn.place(x = 50, y = 270, width = 210)

        # Creating a button to delete the product from the list
        delete_employee_btn = Button(edit_employee_page, text = "Delete Employee -", font = font_specifications_regular, command = delete_employee)
        delete_employee_btn.place(x = 300, y = 270, width = 210)

        # Table

        # Setting the style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight = 28)

        # Change selected color
        # style.map('Treeview', background[('selected','green')])

        # Using the treeview widget
        employee_trv = ttk.Treeview(edit_employee_page, selectmode ='browse', height = 5)

        # Placing the table
        employee_trv.place(x = 50, y = 320)

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

        # Getting data from the database 'employees' table 
        r_set = cursor.execute('''SELECT * from employees LIMIT 0,10''')
        for dt in r_set:
            employee_trv.insert("", 'end', iid = dt[0], text = dt[0], values = (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        def back_to_menu():
            from Menu import Menu
            edit_employee_page.destroy()
            Menu().main()

        # Creating an exit button
        exit_button = Button(edit_employee_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 850, y = 15)
        
        # Creating a back-to-menu button
        back_to_menu_button = Button(edit_employee_page, text = "Back to menu", font = font_specifications_regular, command = back_to_menu)
        back_to_menu_button.place(x = 830, y = 510)

        edit_employee_page.mainloop()