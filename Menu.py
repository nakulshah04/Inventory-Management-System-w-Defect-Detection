'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from tkinter import *

class Menu:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font
        import time

        menu = Tk()
        menu.title('Menu')
        menu.geometry("800x800")
        menu.configure(bg = "#bed2fa")

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        menu.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        menu_page_header = Label(menu, text = "Menu", font = font_specifications_heading, fg = "black", bg = "#bed2fa")
        menu_page_header.place(x = 420, y = 80)

        def go_to_orders():
            from Orders import Orders
            menu.destroy()
            Orders().main()
        
        def go_to_employees():
            from Employee import Employee
            menu.destroy()
            Employee().main()

        def go_to_products():
            from Product import Product
            menu.destroy()
            Product().main()

        def go_to_defect_check():
            from retrialll import Defect_Check
            menu.destroy()
            Defect_Check().main()

        def clock():
            global date, currenttime
            date = time.strftime("%d-%m-%Y")
            currenttime = time.strftime('%H:%M:%S')
            print(date, currenttime)
            datetime_label.config(text = f'   Date: {date}\nTime: {currenttime}')
            datetime_label.after(1000,clock)

        datetime_label = Label(menu, text = "Hello", font = font_specifications_regular, fg = "black", bg = "#bed2fa")
        datetime_label.place(x = 5, y = 5)

        # Start the clock
        clock()
            
        # Creating buttons for all 5 functionalities of the system
        
        orders_btn = Button(menu, text = "Orders", font = font_specifications_regular, width = 20, activeforeground = "black", command = go_to_orders)
        orders_btn.place(x = 350,y = 180)

        products_btn = Button(menu, text = "Products", font = font_specifications_regular, width = 20, command = go_to_products)
        products_btn.place(x = 350,y = 240)

        defect_check_btn = Button(menu, text = "Defect Check", font = font_specifications_regular, width = 20, command = go_to_defect_check)
        defect_check_btn.place(x = 350, y = 300)

        employees_btn = Button(menu, text = "Employees", font = font_specifications_regular, width = 20, command = go_to_employees)
        employees_btn.place(x = 350, y = 360)

        def sign_out():
            from Login import Login
            menu.destroy()
            Login().main()

        # Creating an sign_out_button button
        sign_out_button = Button(menu, text = "Sign Out", font = font_specifications_regular, command = sign_out, width = 8)
        sign_out_button.place(x = 850, y = 15)

        # Creating an exit button
        exit_button = Button(menu, text = "EXIT", font = font_specifications_regular, command = quit, width = 8)
        exit_button.place(x = 830, y = 520)

        # Adding logo
        from PIL import Image, ImageTk
        import urllib.request
        
        url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-tuhsa&psig=AOvVaw1aK5zkt-MzG-G2_xo8h1PT&ust=1676348071181000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCLi05azRkf0CFQAAAAAdAAAAABAJ"
        urllib.request.urlretrieve(url, "image.jpg")

        image = Image.open("image.jpg")
        image = ImageTk.PhotoImage(image)
        image_label = Label(menu, image=image)
        image_label.pack()

        menu.mainloop()