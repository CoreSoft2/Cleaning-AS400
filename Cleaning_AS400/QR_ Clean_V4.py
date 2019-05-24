import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()

results = castit_cursor.execute("select customer, company, address1, address2 from Customer where mastercustomerno is null")

for result in results:
	print result	
'''
for result in results:
	new_cust = castit_cursor.execute("select customerno from Customer where company = ? and customerno <> ?", result[2], result[1]).fetch_first()
	castit_cursor.execute("update customer where customerno = ? set address1 = ?, address2 = ? where customer = ", result[1], result[3], result[4])
	castit_cursor.execute("delete from customer where company = ? and customerno <> ?", result[2], new_cust)


cnxn.commit()
'''
