import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()
cnxn.cursor()

parts_from_as400 = castit_cursor.execute("insert into(part_number, owned_by) values('Woodword, Inc.', 'WOM001')").fetchall()
