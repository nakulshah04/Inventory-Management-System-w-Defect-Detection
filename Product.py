'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from ctypes import alignment
from operator import truediv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.font import Font
import sqlite3
from turtle import left

class Product:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        product_page = Tk()
        product_page.title('Product')
        product_page.geometry("800x800")
        product_page.configure(bg = "#bed2fa")

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        product_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        product_page_header = Label(product_page, text = "Products", font=font_specifications_heading, fg="black", bg="#bed2fa")
        product_page_header.place(x = 410, y = 20)

        def go_to_add_product():
            from AddProduct import Add_Product
            product_page.destroy()
            Add_Product().main()

        def go_to_edit_product():
            from EditProduct import Edit_Product
            product_page.destroy()
            Edit_Product().main()
            
        # Creating buttons and arranging them on the screen
        add_product_btn = Button(product_page, text = "Add Product +", width = 20, font = font_specifications_regular, command = go_to_add_product)
        add_product_btn.place(x = 60, y = 120)
        edit_product_btn = Button(product_page, text = "Edit Product Details", width = 20, font = font_specifications_regular, command = go_to_edit_product)
        edit_product_btn.place(x = 680, y = 120)

        # Table

        # Setting the style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight = 28)

        # Using the treeview widget
        trv = ttk.Treeview(product_page, selectmode ='browse', height = 9)

        # Placing the table
        trv.place(x = 60, y = 180)

        # Number of columns
        trv["columns"] = ("1", "2", "3","4")
        
        # Defining the headings
        trv['show'] = 'headings'
        
        # Defining the width of columns and their lignment 
        trv.column("1", width = 160, anchor ='c')
        trv.column("2", width = 350, anchor ='c')
        trv.column("3", width = 160, anchor ='c')
        trv.column("4", width = 200, anchor ='c')
        
        # Adding headings to columns
        trv.heading("1", text = "Product ID")
        trv.heading("2", text = "Product Name")
        trv.heading("3", text = "HSN Code")
        trv.heading("4", text = "Price per unit")  

        # Getting data from the database 'products' table 
        r_set = cursor.execute('''SELECT * from products LIMIT 0,30''')
        for dt in r_set: 
            trv.insert("", 'end', iid = dt[0], text = dt[0], values = (dt[0],dt[1],dt[2],dt[3]))

        def back_to_menu():
            from Menu import Menu
            product_page.destroy()
            Menu().main()

        # Creating an exit button
        exit_button = Button(product_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 850, y = 15)

        # Creating a back-to-menu button
        back_to_menu_button = Button(product_page, text = "Back to menu", font = font_specifications_regular, command = back_to_menu)
        back_to_menu_button.place(x = 830, y = 510)

        product_page.mainloop()