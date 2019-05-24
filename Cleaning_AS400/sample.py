import pyodbc

server = '127.0.0.1'     # Striker(a.k.a. localhost) server
#server = '192.168.1.21' # Castit server
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

# list configured drivers
# pyodbc.drivers()

# AS400 connection
#cnxn = pyodbc.connect('DSN=as400')

# striker Castit connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)

# get cursor
cursor = cnxn.cursor()

# AS400 query
#rows = cursor.execute('select distinct customerno FROM Customer').fetchall()
rows = cursor.execute('select distinct c.customerno, c.Company, p.owned_by from Customer c inner join part_price p on c.customerno = p.owned_by').fetchall()

#cursor.execute('{EXEC Get_CID @Qty = 1}')

custnos = map(lambda x: x[0].encode('utf-8'), rows)
custnos2 = map(lambda x: x.rstrip(), custnos)

for single_Co_No in custnos2:
    #print single_Co_No       #--- looks like intended value
    #print type(single_Co_No) #--- type string

#Step 1 --- Look up "current_custno" with SELECT * FROM Customer WHERE customerno=<obsolete_custno>    

    #final_answer = cursor.execute("""select customerno ,company from Customer where customerno = ?""", single_Co_No).fetchall() 
    #print final_answer #-- prints out every distinct company name and customerno
    
#Step 2 --- Then update part_price, replacing obsolete_custno with current_custno in OWNED_BY field
    answer = cursor.execute("""select owned_by, part_name from part_price where owned_by = ?""", single_Co_No).fetchall()
    print(answer)
    
    
'''

id = 1
for custno in custnos:
    
    row = cursor.fetchone()
    
    first_join = row[0].encode("utf-8")
    print first_join
    print type(first_join)

    cursor.execute("""
                          select 
                            from * Customer
                           where  = ? AND master = ?
                          """, custno, masterno).fetchall()

    
    print execution
    print type(execution)
'''    
    
