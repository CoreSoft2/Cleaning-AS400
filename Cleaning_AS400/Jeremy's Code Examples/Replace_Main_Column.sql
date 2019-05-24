results = execute('SELECT customerno, company, address1, address2, .. FROM Customer WHERE MASTERCUSTOMERNO IS NULL')

for each result in results:
  new_cust = execute('SELECT customerno FROM Customer WHERE Company=? AND customerno <> ? ORDER BY ADDDATE' result[2], result[1]).fetch_first()
  print("UPDATE Customer WHERE CUSTOMERNO=", result[1]," SET ADDRESS1 = ", result[3], ", ADDRESS2 = ", result[4], ", ... WHERE customerno=", new_cust)
  print('DELETE FROM Customer WHERE Company=', result[2], 'AND customerno <> ', result[2], new_cust)




---Not to be added to above code, but could be useful for queries
SELECT customerno FROM Customer WHERE Company='Jetyd Corporation' AND customerno <> '981' ORDER BY ADDDATE
