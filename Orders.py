'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class Orders:
    
    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        orders_page = Tk()
        orders_page.title('Orders')
        orders_page.geometry("800x800")
        orders_page.configure(bg = "#bed2fa")

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        orders_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        orders_page_header = Label(orders_page, text = "Orders", font=font_specifications_heading, fg="black", bg="#bed2fa")
        orders_page_header.place(x = 410, y = 20)

        def go_to_add_order():
            from AddOrder import Add_Order
            orders_page.destroy()
            Add_Order().main()

        def go_to_edit_order():
            from EditOrder import Edit_Order
            orders_page.destroy()
            Edit_Order().main()

        add_order_btn = Button(orders_page, text = "Add Order +", width = 14, font = font_specifications_regular, command = go_to_add_order)
        add_order_btn.place(x = 60, y = 120)

        edit_order_btn = Button(orders_page, text = "Edit Order", width = 14, font = font_specifications_regular, command = go_to_edit_order)
        edit_order_btn.place(x = 680, y = 120)

        # Table

        # Setting the style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight = 28)

        # Using the treeview widget
        trv = ttk.Treeview(orders_page, selectmode ='browse', height = 5)

        # Placing the table
        trv.place(x = 60, y = 190)

        # Number of columns
        trv["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        
        # Defining the headings
        trv['show'] = 'headings'
        
        # Defining the width of columns and their lignment 
        trv.column("1", width = 60, anchor ='c')
        trv.column("2", width = 170, anchor ='c')
        trv.column("3", width = 100, anchor ='c')
        trv.column("4", width = 220, anchor ='c')
        trv.column("5", width = 100, anchor ='c')
        trv.column("6", width = 80, anchor ='c')
        trv.column("7", width = 120, anchor ='c')
        
        # Adding headings to columns
        trv.heading("1", text = "Order ID")
        trv.heading("2", text = "Company Name")
        trv.heading("3", text = "Date of Order")
        trv.heading("4", text = "Product Name")
        trv.heading("5", text = "Price per unit")
        trv.heading("6", text = "Quantity")
        trv.heading("7", text = "Amount")  

        # Getting data from the database 'products' table 
        r_set = cursor.execute('''SELECT * from orders LIMIT 0,20''')
        for dt in r_set: 
            trv.insert("", 'end', 
            iid = dt[0], 
            text = dt[0], 
            values = (dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6])
            )

        def back_to_menu():
            from Menu import Menu
            orders_page.destroy()
            Menu().main()

        # Creating a back-to-menu button
        back_to_menu_button = Button(
            orders_page, 
            text = "Back to Menu", 
            font = font_specifications_regular, 
            command = back_to_menu
        )
        
        back_to_menu_button.place(x = 820, y = 510)

        # Creating an exit button
        exit_button = Button(orders_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 860, y = 15)

        orders_page.mainloop()