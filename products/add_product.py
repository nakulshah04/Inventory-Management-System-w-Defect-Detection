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

class Add_Product:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        add_product_page = Tk()
        add_product_page.title('Add Product')
        add_product_page.geometry("800x800")
        add_product_page.configure(bg = "#bed2fa")

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        add_product_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        # Adding the heading of dashboard
        add_order_page_header = Label(add_product_page, text = "Add a Product", font=font_specifications_heading, fg="black", bg="#bed2fa")
        add_order_page_header.place(x = 350, y = 20)

        # Adding entry boxes
        product_id = Entry(add_product_page, width = 35, font = font_specifications_regular)
        product_id.insert(0, "Product ID")
        product_id.place(x = 40, y = 100)
        product_name = Entry(add_product_page, width = 35, font = font_specifications_regular)
        product_name.insert(0, "Product Name")
        product_name.place(x = 450, y = 100)
        price_per_unit = Entry(add_product_page, width = 35, font = font_specifications_regular)
        price_per_unit.insert(0, "Price per unit")
        price_per_unit.place(x = 40, y = 145)

        def add_product():
            
            # Checking if price has any alphabet
            price_check1 = price_per_unit.get().isnumeric()

            if price_check1 == False:
                messagebox.showerror("showerror", "Invalid price!")
                
            else:

                # Connecting database
                conn = sqlite3.connect("data.db")
                # Creating a cursor
                cursor = conn.cursor()

                # Add new product
                cursor.execute("INSERT INTO products VALUES (:product_id, :product_name, :hsn_code, :price_per_unit)",
                {
                    'product_id': product_id.get(),
                    'product_name': product_name.get(),
                    'hsn_code': 7326,
                    'price_per_unit': price_per_unit.get()
                })
            
                messagebox.showinfo("showinfo", "Product added successfully!")

                conn.commit()
                conn.close()

                trv.insert(parent = '', index = 'end', text = "", values = (product_id.get(), product_name.get(), 7326, price_per_unit.get(),))
                    
                product_id.delete(0, END)
                product_name.delete(0, END)
                price_per_unit.delete(0, END)

        # Creating a button to add the new product to the list
        add_product_btn = Button(add_product_page, text = "Add Product to list +", font = font_specifications_regular, command = add_product)
        add_product_btn.place(x = 40, y = 190)

        # Products table

        # Setting the style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight = 28)

        # Change selected color
        # style.map('Treeview', background[('selected','green')])

        # Using the treeview widget
        trv = ttk.Treeview(add_product_page, selectmode ='browse', height = 8)

        # Placing the table
        trv.place(x = 40, y = 240)

        # Number of columns
        trv["columns"] = ("1", "2", "3","4")
        
        # Defining the headings
        trv['show'] = 'headings'
        
        # Defining the width of columns and their alignment 
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
            trv.insert("", 'end', iid = dt[0], text = dt[0], values = (dt[0], dt[1], dt[2], dt[3]))

        def back_to_menu():
            from Menu import Menu
            add_product_page.destroy()
            Menu().main()

        # Creating a back-to-menu exit button
        back_to_menu_button = Button(add_product_page, text = "Back to Menu", font = font_specifications_regular, command = back_to_menu)
        back_to_menu_button.place(x = 800, y = 520)

        # Creating an exit button
        exit_button = Button(add_product_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 850, y = 15)

        add_product_page.mainloop()