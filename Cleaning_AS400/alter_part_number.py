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
castit_cursor = cnxn.cursor()

castit_cursor.execute("alter part_price alter part_number char(25)")
