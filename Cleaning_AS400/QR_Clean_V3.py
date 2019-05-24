import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()

as400_conversion = castit_cursor.execute("select castit_custno, CUST_NAME from Castit.dbo.AS400_to_Castit_Customer").fetchall()
cnxn.cursor()


#Function used to find the amount of columns that a company name has under it
def amount_of_columns(company_name):
    return castit_cursor.execute("select count(*) from Customer where company = ?", company_name).fetchval()

#as400_num = map(lambda x: x[0].encode('utf-8'), as400_conversion)
#as400_num2 = map(lambda x: x.rstrip(), as400_num)

as400_nam = map(lambda x: x[1].encode('utf-8').rstrip(), as400_conversion)

for custnam in as400_nam:
    custnam_string = str(custnam, 'utf-8')
    main_custno = str(castit_cursor.execute("select AS400_CUSTNO from AS400_to_Castit_Customer where cust_name = ?", custnam_string).fetchval()).rstrip()
    
    company_instances = castit_cursor.execute("select customerno from Customer where Company = ?", custnam_string).fetchall()
    is_same = False
    amount_of_times_orig = amount_of_columns(custnam_string)
    

    for listed_customer in company_instances:
        if listed_customer[0].rstrip() == main_custno:
            is_same = True
            
    if is_same == True:
        for listed_customer in company_instances:
            print(listed_customer[0], custnam_string)
        print (amount_of_times_orig)
    

    if amount_of_times_orig > 1:
        for listed_customer in company_instances:
            if listed_customer[0] != main_custno:
                current_column = castit_cursor.execute("select * from Customer where customerno = ?", listed_customer[0])
                main_column = castit_cursor.execute("select * from Customer where customerno = ?", main_custno)
                castit_cursor.execute("update Customer set current_column = main_column")

        castit_cursor.execute("delete from Customer where customerno = ?", main_custno)

        if amount_of_times(custnam_string) - 1 > 1:
            while amount_of_times(custnam_string) > 1:
		castit_cursor.execute("delete Customer where customerno = ?", listed_customer[0])
