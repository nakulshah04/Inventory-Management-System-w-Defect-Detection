'''
    INVENTORY MANAGEMENT SYSTEM
    Author: Nakul Shah
'''

import sqlite3

conn = sqlite3.connect("data.db")

# Variable to edit the database
cursor = conn.cursor()

# Create table named 'orders'
cursor.execute('''CREATE TABLE IF NOT EXISTS orders(order_id BIGINT, company_name TEXT, date_of_order DATE, product_name_entry TEXT, price_per_unit_entry BIGINT, enter_quantity INT, amount BIGINT)''')

# Add data to column
cursor.execute('''INSERT INTO orders(order_id, company_name, date_of_order, product_name_entry, price_per_unit_entry, enter_quantity, amount) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('001', 'Asanplast Chemicals', "2022-01-07", "200 NB Elbow with Flange", 9866, 10, (9866*10)))
cursor.execute('''INSERT INTO orders(order_id, company_name, date_of_order, product_name_entry, price_per_unit_entry, enter_quantity, amount) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('002', 'Asanplast Chemicals', "2022-01-22", "40 NB Pipe with Flange - 2m", 1807, 60, (1807*60)))
cursor.execute('''INSERT INTO orders(order_id, company_name, date_of_order, product_name_entry, price_per_unit_entry, enter_quantity, amount) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('003', 'Natulal Engineers', "2022-01-27", "150x80 Ecentric Reducer with Flange", 4056, 22, (4056*22)))
cursor.execute('''INSERT INTO orders(order_id, company_name, date_of_order, product_name_entry, price_per_unit_entry, enter_quantity, amount) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('004', 'Natulal Engineers', "2022-01-27", "ATNB Pipe with Flange - 200mm", 1938, 45, (1938*45)))
cursor.execute('''INSERT INTO orders(order_id, company_name, date_of_order, product_name_entry, price_per_unit_entry, enter_quantity, amount) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('005', 'Natulal Engineers', "2022-01-27", "140x25 CON. Reducer with Flange", 4056, 35, (4056*35)))

# conn.commit() # Save the database

# Create table named 'products'
cursor.execute('''CREATE TABLE IF NOT EXISTS products(product_id BIGINT, product_name TEXT, hsn_code INT, price_per_unit INT)''')

# Add data to column
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('001', "200 NB Elbow with Flange", 7326, 9866))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('002', "50 NB Pipe with Flange - 3m", 7326, 3154))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('003', "100 NB Elbow with Flange", 7326, 2954))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('004', "100x40 CON. Reducer with Flange", 7326, 1850))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('005', "25 NB Pipe with Flange - 3m", 7326, 1872))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('006', "40 NB Pipe with Flange - 2m", 7326, 1807))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('007', "150 NB Elbow with Flange", 7326, 6366))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('008', "150x50 Unequal Tee with Flange", 7326, 5889))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('009', "200x50 Unequal Tee with Flange", 7326, 9259))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('010', "40x25 CON. Reducer with Flange", 7326, 768))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('011', "40 NM Equal Tee with Flange", 7326, 1227))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('012', "ATNB Elbow with Flange", 7326, 2063))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('013', "150x50 CON. Reducer with Flange", 7326, 4219))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('014', "40x25 Reducing Flange", 7326, 626))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('015', "150x80 Ecentric Reducer with Flange", 7326, 4056))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('016', "50 BM Elbow with Flange", 7326, 1178))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('017', "50 NB Jacketed Pipe with Flange - 150mm", 7326, 2670))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('018', "100x80 Reducing Flange", 7326, 1662))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('019', "50 NB Dip Pipe with Flange - 1690mm", 7326, 2541))
cursor.execute('''INSERT INTO products(product_id, product_name, hsn_code, price_per_unit) VALUES(?, ?, ?, ?)''', ('020', "ATNB Pipe with Flange - 200mm", 7326, 1938))

conn.commit() # Save the database

# Create table named 'employees'
cursor.execute('''CREATE TABLE IF NOT EXISTS employees(employee_id BIGINT, employee_name TEXT, employee_dob DATE, employee_mobile_no BIGINT, employee_address TEXT, employee_job_grade TEXT, employee_salary INT)''')
# Add data to column
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('001', "Rajesh Sharma", '1972-02-16', 8903785641,'Ramgad Nagar, Mulund', 'Weldor', 760))
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('002', "Virendar Rathi", '1969-12-30', 9876133200,'Narayan Poli, Dombivili', 'Disk Driller', 640))
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('003', "Ramesh Prajapati", '1985-05-03', 7795643328,'Kalwa Creek, Thane', 'Painter', 590))
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('004', "Kiran Shetty", '1966-10-11', 9223789012,'Teen Hath Naka, Thane', 'Lathe Operator', 620))
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('005', "Smitesh Chauhan", '1977-01-13', 8930161635,'Kamal Ghat, Mulund', 'Painter', 590))
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('006', "Manvinder Singh", '1969-12-30', 9091866814,'Marol Chowk, Kalyan', 'Disk Driller', 640))
cursor.execute('''INSERT INTO employees(employee_id, employee_name, employee_dob, employee_mobile_no, employee_address, employee_job_grade, employee_salary) VALUES(?, ?, ?, ?, ?, ?, ?)''', ('007', "Babulal Kumar", '1969-12-30', 7215156969,'Panchpakhadi, Thane', 'Lathe Operator', 620))

conn.commit() # Save the database