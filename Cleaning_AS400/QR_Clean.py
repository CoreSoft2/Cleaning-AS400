import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()

as400_conversion = castit_cursor.execute("select AS400_CUSTNO, CUST_NAME from Castit.dbo.AS400_to_Castit_Customer").fetchall()
cnxn.cursor()

#as400_num = map(lambda x: x[0].encode('utf-8'), as400_conversion)
#as400_num2 = map(lambda x: x.rstrip(), as400_num)

as400_nam = map(lambda x: x[1].encode('utf-8'), as400_conversion)
as400_nam2 = map(lambda x: x.rstrip(), as400_nam)

for custnam in as400_nam2:
    custnam_string = str(custnam, 'utf-8')
    main_custno = str(castit_cursor.execute("select AS400_CUSTNO from AS400_to_Castit_Customer where cust_name = ?", custnam_string).fetchval()).rstrip()
    
    company_instances = castit_cursor.execute("select customerno from Customer where Company = ?", custnam_string).fetchall()
    is_same = False
    for listed_customer in company_instances:
        if listed_customer[0].rstrip() == main_custno:
            is_same = True
            #break
        #print(listed_customer[0].rstrip(), main_custno)
        #print(is_same)
    
    if is_same == True:
        for listed_customer in company_instances:
            print(listed_customer[0], custnam_string)

    
