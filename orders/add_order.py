'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import date

class Add_Order:

    def __init__(self):
        pass
    
    def main(self):
        
        from tkinter import ALL
        from tkinter.font import Font

        add_order_page = Tk()
        add_order_page.title('Add Order')
        add_order_page.geometry("800x800")
        add_order_page.configure(bg = "#bed2fa")

        # count_order = 1

        # Connecting database
        conn = sqlite3.connect("data.db")
        # Creating a cursor
        cursor = conn.cursor()

        # Dimensions of window
        width = 1000
        height = 600

        # Sets the upper-left coordinate of the window
        add_order_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

        font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
        font_specifications_regular = Font(family = "Avenir Next", size = 18)

        def back_to_menu():
            from Menu import Menu
            add_order_page.destroy()
            Menu().main()

        # Creating a back-to-menu button
        back_to_menu_button = Button(add_order_page, text = "Back to menu", font = font_specifications_regular, command = back_to_menu)
        back_to_menu_button.place(x = 830, y = 540)

        # Adding the header
        add_order_page_header = Label(add_order_page, text = "Add an Order", font=font_specifications_heading, fg="black", bg="#bed2fa")
        add_order_page_header.place(x = 350, y = 20)

        # # Adding a sign out button at top-right
        # sign_out = Button(add_order_page, text = "X | Sign Out", command = add_order_page.quit, font = font_specifications_regular)
        # sign_out.place(x = 850, y = 10)

        # Adding entry boxes for company name and est. delivery date
        company_name = Entry(add_order_page, width = 40, font = font_specifications_regular)
        company_name.insert(0, "Company Name")
        company_name.place(x = 40, y = 100)
        
        date_of_order = Entry(add_order_page, width = 40, font = font_specifications_regular)
        today = date.today()
        date_of_order.insert(0, today)
        date_of_order.place(x = 40, y = 145)

        # Creating entry boxes/labels for product name, quantity, price per unit, amount

        product_id = Label(add_order_page, text = "Product ID", bg = "#bed2fa", font = font_specifications_regular)
        product_id.place(x = 530, y = 100)
        product_id_entry = Entry(add_order_page, width = 20, font = font_specifications_regular)
        product_id_entry.insert(0, "")
        product_id_entry.place(x = 680, y = 100)

        product_name = Label(add_order_page, text = "Product Name", bg = "#bed2fa", font = font_specifications_regular)
        product_name.place(x = 530, y = 145)
        product_name_entry = Entry(add_order_page, width = 20, font = font_specifications_regular)
        product_name_entry.insert(0, "")
        product_name_entry.place(x = 680, y = 145)

        quantity = Label(add_order_page, text = "Quantity:", bg = "#bed2fa", font = font_specifications_regular)
        quantity.place(x = 530, y = 190)
        enter_quantity = Entry(add_order_page, width = 20, font = font_specifications_regular)
        enter_quantity.insert(0, "")
        enter_quantity.place(x = 680, y = 190)

        price_per_unit = Label(add_order_page, text = "Price Per Unit:", bg = "#bed2fa", font = font_specifications_regular)
        price_per_unit.place(x = 530, y = 235)
        price_per_unit_entry = Entry(add_order_page, width = 20, font = font_specifications_regular)
        price_per_unit_entry.insert(0, "")
        price_per_unit_entry.place(x = 680, y = 235)

        def add_to_cart():
            
            # Checking if quantity has any alphabet
            quantity_check_1 = enter_quantity.get().isnumeric()
            quantity_check_2 = int(enter_quantity.get()) > 0
            company_name_check = True
            date_of_order_check = True

            if (len(company_name.get()) == 0) or (len(date_of_order.get()) == 0):
                if (len(company_name.get()) == 0):
                    company_name_check = False
                else:
                    date_of_order_check = False

            if quantity_check_1 == False or quantity_check_2 == False or company_name_check == False or date_of_order_check == False:
                if company_name_check == False:
                    messagebox.showerror("showerror", "Company name cannot be empty!")
                else:
                    if date_of_order_check == False:
                        messagebox.showerror("showerror", "Invalid date of order!")
                    else:
                        if quantity_check_1 == False:
                            messagebox.showerror("showerror", "Invalid quantity!")
                        else:
                            messagebox.showerror("showerror", "Quantity cannot be negative!")
            else:
                # Connecting database
                conn = sqlite3.connect("data.db")
                # Creating a cursor
                c = conn.cursor()
                # Creating a table
                c.execute('''CREATE TABLE IF NOT EXISTS orders(order_id BIGINT, company_name TEXT, date_of_order DATE, product_name_entry TEXT, price_per_unit_entry BIGINT, enter_quantity INT, amount BIGINT)''')
                # Adding rows
                c.execute("INSERT INTO orders VALUES (:order_id, :company_name, :date_of_order, :product_name_entry, :price_per_unit_entry, :enter_quantity, :amount)",
                {
                    'order_id': 6,
                    'company_name': company_name.get(),
                    'date_of_order': date_of_order.get(),
                    'product_name_entry': product_name_entry.get(),
                    'price_per_unit_entry': price_per_unit_entry.get(),
                    'enter_quantity': enter_quantity.get(),
                    'amount': int(price_per_unit_entry.get()) * int(enter_quantity.get()),
                })
                messagebox.showinfo("showinfo", "Product added to cart successfully!")
                conn.commit()
                conn.close()

                order_trv.insert(parent = '', index = 'end', text = "", values = (6, company_name.get(), date_of_order.get(), product_name_entry.get(), price_per_unit_entry.get(), enter_quantity.get(), int(price_per_unit_entry.get()) * int(enter_quantity.get()),))
                # Clearing all boxes
                # company_name.delete(0, END)
                # date_of_order.delete(0, END)
                product_id_entry.delete(0, END)
                product_name_entry.delete(0, END)
                price_per_unit_entry.delete(0, END)
                enter_quantity.delete(0, END)

        # Creating buttons
        add_product = Button(add_order_page, text = "Add to cart", width = 12, font = font_specifications_regular, command = add_to_cart)
        add_product.place(x = 530, y = 290)
        delete_product = Button(add_order_page, text = "Delete from cart", width = 12, font = font_specifications_regular)
        delete_product.place(x = 745, y = 290)

        # Orders table

        # Setting the style
        style2 = ttk.Style()
        style2.configure('Treeview', rowheight = 25)
        style2.theme_use('clam')

        # Using the treeview widget
        order_trv = ttk.Treeview(add_order_page, selectmode ='browse', height = 5)

        # Placing the table
        order_trv.place(x = 40, y = 375)

        # Number of columns
        order_trv["columns"] = ("1", "2", "3","4","5","6","7")
        
        # Defining the headings
        order_trv['show'] = 'headings'
        
        # Defining the width of columns and their alignment 
        order_trv.column("1", width = 60, anchor ='c')
        order_trv.column("2", width = 180, anchor ='c')
        order_trv.column("3", width = 100, anchor ='c')
        order_trv.column("4", width = 240, anchor ='c')
        order_trv.column("5", width = 100, anchor ='c')
        order_trv.column("6", width = 100, anchor ='c')
        order_trv.column("7", width = 100, anchor ='c')
        
        # Adding headings to columns
        order_trv.heading("1", text = "Order ID")
        order_trv.heading("2", text = "Company Name")
        order_trv.heading("3", text = "Date of order")
        order_trv.heading("4", text = "Product Name")  
        order_trv.heading("5", text = "Quantity")
        order_trv.heading("6", text = "Price per unit")
        order_trv.heading("7", text = "Amount")

        # Getting data from the database 'products' table 
        r_set_1 = cursor.execute('''SELECT * from orders LIMIT 0,10''')
        for dt in r_set_1: 
            order_trv.insert("", 'end', text = dt[0], values = (dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6]))

        def product_selected():
            
            # Grabbing the product details
            product_selected = product_trv.focus()
            product_details = product_trv.item(product_selected, 'values')

            # Filling in the values
            product_id_entry.insert(0, product_details[0])
            product_name_entry.insert(0, product_details[1])
            # enter_quantity.insert(0, product_details[2])
            price_per_unit_entry.insert(0, product_details[3])
            # amount_entry.insert(0, product_details[5])

        select_product = Button(add_order_page, text = "Select Product", width = 15, font = font_specifications_regular, command = product_selected)
        select_product.place(x = 40, y = 325)

        # Products table

        # Setting the style
        style1 = ttk.Style()
        style1.configure('Treeview', rowheight = 25)
        style1.theme_use('clam')

        # Change selected color
        # style.map('Treeview', background[('selected','green')])

        # Using the treeview widget
        product_trv = ttk.Treeview(add_order_page, selectmode ='browse', height = 4)

        # Placing the table
        product_trv.place(x = 40, y = 190)

        # Number of columns
        product_trv["columns"] = ("1", "2", "3","4")
        
        # Defining the headings
        product_trv['show'] = 'headings'
        
        # Defining the width of columns and their alignment 
        product_trv.column("1", width = 40, anchor ='c')
        product_trv.column("2", width = 270, anchor ='c')
        product_trv.column("3", width = 50, anchor ='c')
        product_trv.column("4", width = 85, anchor ='c')
        
        # Adding headings to columns
        product_trv.heading("1", text = "ID")
        product_trv.heading("2", text = "Product Name")
        product_trv.heading("3", text = "HSN")
        product_trv.heading("4", text = "Price per unit")  

        # Getting data from the database 'products' table 
        r_set_2 = cursor.execute('''SELECT * from products LIMIT 0,30''')
        for dt in r_set_2: 
            product_trv.insert("", 'end',iid = dt[0], text = dt[0], values = (dt[0],dt[1],dt[2],dt[3]))

        # Creating an exit button
        exit_button = Button(add_order_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
        exit_button.place(x = 850, y = 15)

        def add_new_order():
            add_order_page.destroy()
            Add_Order().main()

        # Add a new order
        add_new_order_button = Button(add_order_page, text = "Add New Order", font = font_specifications_regular, command = add_new_order, width = 15)
        add_new_order_button.place(x = 40, y = 540)

        add_order_page.mainloop()

# Add_Order().main()