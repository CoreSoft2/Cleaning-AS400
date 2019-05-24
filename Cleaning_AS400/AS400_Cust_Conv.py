import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()
cnxn.cursor()


as400_conversion = castit_cursor.execute("select as400_custno, CUST_NAME from Castit.dbo.AS400_to_Castit_Customer").fetchall()

castit_conversion = castit_cursor.execute("select mastercustomerno from castit.dbo.Customer").fetchall()

as400_numbers = map(lambda x: x[0], as400_conversion)
customer_names = map(lambda x: x[1].encode('utf-8').rstrip(), as400_conversion)
master_customer_numbers = map(lambda x: x[0].encode('utf-8').rstrip(), castit_conversion)

for as400_num in as400_numbers:
        #company_num_string = as400_num
        company_name = castit_cursor.execute("select cust_name from AS400_to_Castit_Customer where as400_custno = ?", as400_num).fetchval()#.rstrip()

        #master_customer_nos = castit_cursor.execute("select mastercustomerno from Customer where company = ? '''and mastercustomerno like '%[A-Z]%'", company_name).fetchall()
        master_customer_list = castit_cursor.execute("select mastercustomerno from Customer where company = ? and mastercustomerno is not null and Customerno like '%[A-Z]%'", company_name).fetchall()
        #master_customer_nos = map(lambda x: x[0].encode('utf-8').rstrip(), master_customer_list)
        #new_mastercustomerno = master_customer_nos[0]#.rstrip()
        if master_customer_list:                
                new_mastercustomerno = str(master_customer_list[0])
                new_mastercustomerno = new_mastercustomerno.replace("(", "")
                new_mastercustomerno = new_mastercustomerno.replace("'", "")
                new_mastercustomerno = new_mastercustomerno.replace(" ", "")
                new_mastercustomerno = new_mastercustomerno.replace(",", "")
                new_mastercustomerno = new_mastercustomerno.replace(")", "")

                print(as400_num, company_name, new_mastercustomerno)

                castit_cursor.execute("update AS400_to_Castit_Customer set castit_custno = ? where cust_name = ?", new_mastercustomerno, company_name)

cnxn.commit()
