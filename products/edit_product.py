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

class Edit_Product:
	
	def __init__(self):
		pass

	def main(self):
		from tkinter import ALL
		from tkinter.font import Font
		
		edit_product_page = Tk()
		edit_product_page.title('Edit Product')
		edit_product_page.geometry("800x800")
		edit_product_page.configure(bg = "#bed2fa")

		# Connecting database
		conn = sqlite3.connect("data.db")
		# Creating a cursor
		cursor = conn.cursor()

		# Dimensions of window
		width = 1000
		height = 600

		# Sets the upper-left coordinate of the window
		edit_product_page.geometry("%dx%d+%d+%d" % (width, height, 220, 150))

		font_specifications_heading = Font(family = "Avenir Next", size = 36, underline = TRUE)
		font_specifications_regular = Font(family = "Avenir Next", size = 18)

		# Adding the header
		edit_order_page_header = Label(edit_product_page, text = "Edit a Product", font=font_specifications_heading, fg="black", bg="#bed2fa")
		edit_order_page_header.place(x = 350, y = 20)

		# Adding entry boxes
		product_name = Entry(edit_product_page, width = 35, font = font_specifications_regular)
		product_name.insert(0, "Product Name")
		product_name.place(x = 50, y = 95)
		product_id = Entry(edit_product_page, width = 35, font = font_specifications_regular)
		product_id.insert(0, "Product ID")
		product_id.place(x = 500, y = 95)
		hsn_code = Entry(edit_product_page, width = 35, font = font_specifications_regular)
		hsn_code.insert(0, "HSN code")
		hsn_code.place(x = 50, y = 145)
		price_per_unit = Entry(edit_product_page, width = 35, font = font_specifications_regular)
		price_per_unit.insert(0, "Price per unit")
		price_per_unit.place(x = 500, y = 145)

		def product_selected():
			# Grabbing the product details
			product_selected = product_trv.focus()
			product_details = product_trv.item(product_selected, 'values')
			# Clearing the values
			product_id.delete(0, END)
			product_name.delete(0, END)
			hsn_code.delete(0, END)
			price_per_unit.delete(0, END)
			# Filling in the values
			product_id.insert(0, product_details[0])
			product_name.insert(0, product_details[1])
			hsn_code.insert(0, product_details[2])
			price_per_unit.insert(0, product_details[3])

		# Edit product
		def edit_product():

			# Grab the record number
			selected = product_trv.focus()
			# Update record
			product_trv.item(selected, text = "", values = (product_id.get(), product_name.get(), 7326, price_per_unit.get(),))

			# Connect to database
			conn = sqlite3.connect('data.db')
			# Create a cursor instance
			c = conn.cursor()

			c.execute("""UPDATE products SET
				product_id = :product_id,
				product_name = :product_name,
				hsn_code = :hsn_code,
				price_per_unit = :price_per_unit

				WHERE product_id = :product_id""",
				{
					'product_id': product_id.get(),
					'product_name': product_name.get(),
					'hsn_code': hsn_code.get(),
					'price_per_unit': price_per_unit.get(),
				})

			# Commit changes
			conn.commit()
			# Close our connection
			conn.close()

			messagebox.showinfo("showinfo", "Produt edited successfully!")

			# Clear entry boxes
			product_id.delete(0, END)
			product_name.delete(0, END)
			hsn_code.delete(0, END)
			price_per_unit.delete(0, END)

		# Remove one record
		def delete_product():
			
			answer = messagebox.askyesno("askyesno", "Are you sure you want to delete the product?")
			
			if answer:

				x = product_trv.selection()
				product_trv.delete(x)
				
				# Connect to database
				conn = sqlite3.connect('data.db')
				# Create a cursor instance
				cursor = conn.cursor()

				# Deleting from database
				cursor.execute("""DELETE FROM products
					WHERE product_id = :product_id""", 
				{
					'product_id': product_id.get()
				})

				# Clearing entry boxes
				product_id.delete(0, END)
				product_name.delete(0, END)
				hsn_code.delete(0, END)
				price_per_unit.delete(0, END)

				# Commit changes
				conn.commit()
				# Close our connection
				conn.close()

			else:
				pass

		# Creating a button to save the edited product to the list
		save_changes_btn = Button(edit_product_page, text = "Save Changes", font = font_specifications_regular, command = edit_product)
		save_changes_btn.place(x = 50, y = 200, width = 210)
		# Creating a button to delete the product from the list
		delete_product_btn = Button(edit_product_page, text = "Delete Product -", font = font_specifications_regular, command = delete_product)
		delete_product_btn.place(x = 300, y = 200, width = 210)

		# Table

		# Setting the style
		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Treeview', rowheight = 28)

		# Using the treeview widget
		product_trv = ttk.Treeview(edit_product_page, selectmode = 'browse', height = 7)

		# Placing the table
		product_trv.place(x = 50, y = 250)

		# Number of columns
		product_trv["columns"] = ("1", "2", "3","4")

		# Defining the headings
		product_trv['show'] = 'headings'

		# Defining the width of columns and their alignment 
		product_trv.column("1", width = 150, anchor ='c')
		product_trv.column("2", width = 345, anchor ='c')
		product_trv.column("3", width = 150, anchor ='c')
		product_trv.column("4", width = 200, anchor ='c')

		# Adding headings to columns
		product_trv.heading("1", text = "Product ID")
		product_trv.heading("2", text = "Product Name")
		product_trv.heading("3", text = "HSN Code")
		product_trv.heading("4", text = "Price per unit")  

		# Getting data from the database 'products' table 
		r_set = cursor.execute('''SELECT * from products LIMIT 0,30''')
		for dt in r_set: 
			product_trv.insert("", 'end', iid = dt[0], text = dt[0], values = (dt[0],dt[1],dt[2],dt[3]))

		select_product = Button(edit_product_page, text = "Select Product", width = 12, font = font_specifications_regular, command = product_selected)
		select_product.place(x = 50, y = 490, width = 200)

		def go_to_menu():
			from Menu import Menu
			edit_product_page.destroy()
			Menu().main()

        # Creating a back-to-menu exit button
		back_to_menu_button = Button(edit_product_page, text = "Back to Menu", font = font_specifications_regular, command = go_to_menu)
		back_to_menu_button.place(x = 800, y = 520)

        # Creating an exit button
		exit_button = Button(edit_product_page, text = "EXIT", font = font_specifications_regular, command = quit, width = 6)
		exit_button.place(x = 850, y = 15)
		
		edit_product_page.mainloop()