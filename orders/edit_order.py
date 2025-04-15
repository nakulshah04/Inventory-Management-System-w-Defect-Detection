'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

from ctypes import alignment
from itertools import product
from operator import truediv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
from turtle import left
from urllib.request import ProxyDigestAuthHandler

class Edit_Order:
	
	def __init__(self):
		pass

	def main(self):
		from tkinter import ALL
		from tkinter.font import Font
		
		edit_order_page = Tk()
		edit_order_page.title('Edit Order')
		edit_order_page.geometry("800x800")
		edit_order_page.configure(bg = "#bed2fa")

		# Connecting database
		conn = sqlite3.connect("data.db")
		# Creating a cursor
		cursor = conn.cursor()

		# Dimensions of window
		width = 1000
		height = 600

		# Sets the upper-left coordinate of the window
		edit_order_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

		font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
		font_specifications_regular = Font(family = "Avenir Next", size = 18)

		# Adding the header
		edit_order_page_header = Label(edit_order_page, text = "Edit an Order", font=font_specifications_heading, fg="black", bg="#bed2fa")
		edit_order_page_header.place(x = 350, y = 20)

		# Adding entry boxes for company name and order date
		company_name = Entry(edit_order_page, width = 35, font = font_specifications_regular)
		company_name.insert(0, "Company Name")
		company_name.place(x = 40, y = 100)
		date_of_order = Entry(edit_order_page, width = 35, font = font_specifications_regular)
		date_of_order.insert(0, "Date of order (YYYY-MM-DD)")
		date_of_order.place(x = 40, y = 145)

		# Creating entry boxes/labels for product name, quantity, price per unit, amount
		# product_id = Label(edit_order_page, text = "Product ID", bg = "#bed2fa", font = font_specifications_regular)
		# product_id.place(x = 530, y = 100)
		# product_id_entry = Entry(edit_order_page, width = 20, font = font_specifications_regular)
		# product_id_entry.insert(0, "")
		# product_id_entry.place(x = 680, y = 100)

		product_name = Label(edit_order_page, text = "Product Name", bg = "#bed2fa", font = font_specifications_regular)
		product_name.place(x = 470, y = 100)
		product_name_entry = Entry(edit_order_page, width = 27, font = font_specifications_regular)
		product_name_entry.insert(0, "")
		product_name_entry.place(x = 620, y = 100)

		quantity = Label(edit_order_page, text = "Quantity:", bg = "#bed2fa", font = font_specifications_regular)
		quantity.place(x = 470, y = 145)
		enter_quantity = Entry(edit_order_page, width = 27, font = font_specifications_regular)
		enter_quantity.insert(0, "")
		enter_quantity.place(x = 620, y = 145)

		price_per_unit = Label(edit_order_page, text = "Price Per Unit:", bg = "#bed2fa", font = font_specifications_regular)
		price_per_unit.place(x = 470, y = 190)
		price_per_unit_entry = Entry(edit_order_page, width = 27, font = font_specifications_regular)
		price_per_unit_entry.insert(0, "")
		price_per_unit_entry.place(x = 620, y = 190)

		def order_selected():
			# Grabbing the order details
			order_selected = order_trv.focus()
			order_details = order_trv.item(order_selected, 'values')
			# Clearing the values
			company_name.delete(0, END)
			date_of_order.delete(0, END)
			# product_id_entry.delete(0, END)
			product_name_entry.delete(0, END)
			enter_quantity.delete(0, END)
			price_per_unit_entry.delete(0, END)
			# Filling in the values
			company_name.insert(0, order_details[1])
			date_of_order.insert(0, order_details[2])
			# product_id_entry.insert(0, order_details[0])
			product_name_entry.insert(0, order_details[3])
			enter_quantity.insert(0, order_details[5])
			price_per_unit_entry.insert(0, order_details[4])

		# Edit order
		def edit_order():

			# Grabbing the order details
			order_selected = order_trv.focus()
			order_details = order_trv.item(order_selected, 'values')

			# Update record
			order_trv.item(order_selected, text = "", values = (order_details[0], company_name.get(), date_of_order.get(), product_name_entry.get(), price_per_unit_entry.get(), enter_quantity.get(), (int(price_per_unit_entry.get()) * int(enter_quantity.get())),))
			# order_trv.item(order_selected, text = "", values = (order_details[0], company_name.get(), date_of_order.get(), product_name_entry.get(), price_per_unit_entry.get(), enter_quantity.get(), 500,))

			# Connect to database
			conn = sqlite3.connect('data.db')
			# Create a cursor instance
			cursor = conn.cursor()

			cursor.execute("""UPDATE orders SET
				order_id = :order_id,
				company_name = :company_name,
				date_of_order = :date_of_order,
				product_name_entry = :product_name_entry,
				enter_quantity = :enter_quantity,
				price_per_unit_entry = :price_per_unit_entry,
				amount = :amount

				WHERE order_id = :order_id""",
				{
					'order_id': order_details[0],
					'company_name': company_name.get(),
					'date_of_order': date_of_order.get(),
					'product_name_entry': product_name_entry.get(),
					'enter_quantity': enter_quantity.get(),
					'price_per_unit_entry': price_per_unit_entry.get(),
					'amount': (int(price_per_unit_entry.get()) * int(enter_quantity.get())),
				})

			# Commit changes
			conn.commit()
			# Close our connection
			conn.close()

			messagebox.showinfo("showinfo", "Order edited successfully!")

			# Clear entry boxes
			company_name.delete(0, END)
			date_of_order.delete(0, END)
			# product_id_entry.delete(0, END)
			product_name_entry.delete(0, END)
			enter_quantity.delete(0, END)
			price_per_unit_entry.delete(0, END)

		# Remove one record
		def delete_order():

			answer = messagebox.askyesno("askyesno", "Are you sure you want to delete the order?")

			if answer:
				
				order_selected = order_trv.focus()
				order_details = order_trv.item(order_selected, 'values')
				
				# Connect to database
				conn = sqlite3.connect('data.db')
				# Create a cursor instance
				cursor = conn.cursor()
				# Deleting from database
				
				cursor.execute("DELETE FROM orders WHERE order_id=" + order_details[0])

				# Clearing entry boxes
				company_name.delete(0, END)
				date_of_order.delete(0, END)
				product_name_entry.delete(0, END)
				enter_quantity.delete(0, END)
				price_per_unit_entry.delete(0, END)

				# Commit changes
				conn.commit()
				# Close our connection
				conn.close()

			else:
				pass

		# Creating a button to save the edited product to the list
		save_changes_btn = Button(edit_order_page, text = "Save Changes", font = font_specifications_regular, command = edit_order)
		save_changes_btn.place(x = 40, y = 200, width = 180)
		# Creating a button to delete the product from the list
		delete_order_btn = Button(edit_order_page, text = "Delete Order -", font = font_specifications_regular, command = delete_order)
		delete_order_btn.place(x = 255, y = 200, width = 180)

		# Orders table

		# Setting the style
		style = ttk.Style()
		style.configure('Treeview', rowheight = 25)
		style.theme_use('clam')

		# Using the treeview widget
		order_trv = ttk.Treeview(edit_order_page, selectmode = 'browse', height = 5)

		# Placing the table
		order_trv.place(x = 40, y = 280)

		# Number of columns
		order_trv["columns"] = ("1", "2", "3","4","5","6","7")
		
		# Defining the headings
		order_trv['show'] = 'headings'
		
		# Defining the width of columns and their alignment 
		order_trv.column("1", width = 60, anchor ='c')
		order_trv.column("2", width = 180, anchor ='c')
		order_trv.column("3", width = 100, anchor ='c')
		order_trv.column("4", width = 250, anchor ='c')
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

		select_order = Button(edit_order_page, text = "Select Order", width = 12, font = font_specifications_regular, command = order_selected)
		select_order.place(x = 50, y = 485, width = 200)

		def back_to_menu():
			from Menu import Menu
			edit_order_page.destroy()
			Menu().main()

		# Creating an exit button
		exit_button = Button(edit_order_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
		exit_button.place(x = 850, y = 15)

		# Back to menu button
		back_to_menu_button = Button(edit_order_page, text = "Back to Menu", font = font_specifications_regular, command = back_to_menu)
		back_to_menu_button.place(x = 800, y = 520)

		edit_order_page.mainloop()

# Edit_Order().main()