import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()

results = castit_cursor.execute("select customerno, company, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company is not null"). fetchall()

for result in results:
	new_cust = castit_cursor.execute("select customerno from Customer where company = ? and customerno <> ?", result.company, result.customerno).fetchval().rstrip()

	print(result.customerno, new_cust, result.company)
	## print("update Customer set company = {0}, address1 = {1}, address2 = {2}, city = {3}, state = {4}, zip = {5}, country = {6}, contact = {7}, phone = {8}, fax = {9} where customerno = {10}".format(result.company, result.address1, result.address2, result.city, result.state, result.zip, result.country, result.contact, result.phone, result.fax, new_cust))

	castit_cursor.execute("update Customer set company = ?, address1 = ?, address2 = ?, city = ?, state = ?, zip = ?, country = ?, contact = ?, phone = ?, fax = ? where customerno = ?", result.company, result.address1, result.address2, result.city, result.state, result.zip, result.country, result.contact, result.phone, result.fax, new_cust)
	castit_cursor.execute("delete from Customer where company = ? and customerno <> ?", result.company, new_cust)

cnxn.commit()
