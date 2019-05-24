import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()
'''
def row_change(row, array_number):
        row =  = map(lambda x: str(x[array_number].encode('utf-8').rstrip()), row)
        for each_instance in row:
                each_instance = each_instance.replace("b", "")
                each_instance = each_instance.replace("'", "")
        return row[array_number]
'''

def takeout_added_text( given_string ):
        given_string = given_string.replace("b'", "")
        given_string = given_string.replace("'", "")

### JF - Note for Stephen:
###
### The .encode('utf-8') is making the string binary:
###
### >>> results = castit_cursor.execute("select customerno, company, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company is not null").fetchall()
### >>> sample = results.pop()
### >>> sample
### ('961       ', 'Williams International', '3450 Sam Williams Drive', '', 'Ogden', 'UT        ', '84401          ', 'USA                 ', 'Nathan Corey', '8013956593          ', '8016256924          ')
### >>> sample[0]
### '3 Dimensional Engineering'
### >>> sample[0].encode('utf-8')
### b'3 Dimensional Engineering'
###
### So I would just skip the utf-8 encoding (ie. the call toe .encode('utf-8'))
### For company_names below:
###
### company_names = map(lambda x: str(x[1].rstrip()), results)
###
### Additionally, I don't think it's necessary to wrap the returned results in str() call if the columns returned are already strings
        
results = castit_cursor.execute("select customerno, company, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company is not null").fetchall()

# company_names = map(lambda x: str(x[1].encode('utf-8').rstrip()), results)

### JF - same as above but removed the .encode('utf-8)
company_names = map(lambda x: str(x.company.rstrip()), results)

for company_name in company_names:
        #company_name = company_name.replace("b'", "")
        #company_name = company_name.replace("'", "")

        # orig_cust = str(castit_cursor.execute("select customerno, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company = ?", company_name).fetchval().encode('utf-8').rstrip())
        # orig_cust = orig_cust.replace("b'", "")
        # orig_cust = orig_cust.replace("'", "")

        ### JF - same as above but removed the .encode('utf-8) and the str() wrapper
        ### Also changed fetchval() to fetchone(), so orig_cust has all the fields you selected 
        orig_cust = castit_cursor.execute("select customerno, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company = ?", company_name).fetchone()
        ## (orig_customerno, orig_address1, orig_address2, orig_city, orig_state, orig_zip, orig_country, orig_contact, orig_phone, orig_fax) = castit_cursor.execute("select customerno, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company = ?", company_name).fetchone()

        # new_cust = str(castit_cursor.execute("select customerno from Customer where company = ? and customerno <> ?", company_name, orig_cust).fetchval().encode('utf-8').rstrip())
        # new_cust = new_cust.replace("b'", "")
        # new_cust = new_cust.replace("'", "")

        ### JF - same as above but removed the .encode('utf-8) and the str() wrapper
        ### Updated orig_cust to orig_cust[0] to access the customerno field
        new_cust = castit_cursor.execute("select customerno from Customer where company = ? and customerno <> ?", company_name, orig_cust.customerno).fetchval().rstrip()

        ### JF - Updated orig_cust to orig_cust[0] to access the customerno field
        print(company_name, orig_cust.customerno, new_cust)
        
'''
null_customer_numbers = map(lambda x: int(x[0].encode('utf-8'), results)


        
for company_name in company_names:
	new_cust = castit_cursor.execute("select customerno from Customer where company = ? and customerno <> ?", company_name, null_customer_numbers).fetch_first()
	print new_cust
        #castit_cursor.execute("update customer set address1 = ?, address2 = ? where customer = ?", result[3], result[4], result.customerno)
	#castit_cursor.execute("delete from customer where company = ? and customerno <> ?", result[2], new_cust)


cnxn.commit()
'''
