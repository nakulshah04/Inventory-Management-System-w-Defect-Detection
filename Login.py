from multiprocessing import Value
from tkinter import *
from tkinter import messagebox
from setuptools import Command

class Login:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        login = Tk()
        login.title('Login Page')
        login.geometry("800x800")
        login.configure(bg = "#bed2fa")

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        login.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_main = Font(family = "Avenir Next", size = 36, weight = "bold")
        font_specifications_heading = Font(family = "Avenir Next", size = 33, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of the system
        system_header = Label(login, text = "INVENTORY MANAGEMENT SYSTEM", font = font_specifications_main, fg = "black", bg = "#bed2fa")
        system_header.place(x = 180, y = 30)
        
        # Adding the heading of login
        login_header = Label(login, text = "Login", font = font_specifications_heading, fg = "black", bg = "#bed2fa")
        login_header.place(x = 435, y = 130)

        validated_username = "admin"
        validated_password = "admin"

        def hide_password():
            if password.cget('show') == '*':
                password.config(show = '')
            else:
                password.config(show = '*')

        hide_btn = Button(login, text = "Show Password", command = hide_password, font = font_specifications_regular)
        hide_btn.place(x = 535, y = 300)

        # Creating entry boxes for username and password
        username = Entry(login, width = 35, font = font_specifications_regular)
        username.insert(0, "Enter Username")
        username.place(x = 120, y = 250)
        password = Entry(login, width = 35, show = '*', font = font_specifications_regular)
        password.insert(0, "Enter Password")
        password.place(x = 120, y = 300)

        # Creating labels
        username_label = Label(login, text = "Username", bg = "#bed2fa", font = font_specifications_regular)
        username_label.place(x = 20, y = 250)
        password_label = Label(login, text = "Password", bg = "#bed2fa", font = font_specifications_regular)
        password_label.place(x = 20, y = 300)

        def submit():
            username_input = username.get()
            password_input = password.get()

            if len(username_input) == 0:
                messagebox.showinfo("showinfo", "Username cannot be empty!")
            else:
                if len(password_input) == 0:
                    messagebox.showinfo("showinfo", "Password cannot be empty!")
                else:
                    # Validation
                    if(username_input == validated_username):
                        if(password_input == validated_password):
                            messagebox.showinfo("showinfo", "Login successful!")
                            success()
                        else:
                            messagebox.showinfo("showinfo", "Password incorrect")
                    else:
                        messagebox.showinfo("showinfo", "Username incorrect")
                        fail()

        # Login successful
        def success():
            login.destroy()
            from Menu import Menu
            Menu().main()

        # Login failure
        def fail():
            # messagebox.showinfo("showinfo", "The username or password is incorrect")
            username.delete(0, END)
            password.delete(0, END)

        # Creating a submit button
        login_btn = Button(login, text = "Login", command = submit, font = font_specifications_regular)
        login_btn.place(x = 120, y = 350, width = 180)

        # Creating an exit button
        exit_button = Button(login, text = "EXIT", font = font_specifications_regular, command = quit)
        exit_button.place(x = 870, y = 510)

        login.mainloop()

# Login().main()