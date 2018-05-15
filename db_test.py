
''' Pymysql test '''

import pymysql.cursors
import pymysql

# Connect to the database
dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = "Julian"
dbName          = "Visits1"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor

# db = Visits1, table = visits, rows(records) = userid (int) / name / visits (int)

cusrorType = pymysql.cursors.DictCursor
connectionObject = pymysql.connect(
									host=dbServerName,
									user=dbUser,
									password=dbPassword,
                                	db=dbName, charset=charSet,cursorclass=cusrorType)

try:
                                   
    # Create a cursor object
    cursorObject = connectionObject.cursor()                                     

    # SQL query string
    sqlQuery = "select * from visits"

    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    cursorObject.execute("INSERT INTO visits(userid[0]) VALUES (1)")

    #Fetch all the rows
    rows = cursorObject.fetchall()

    for row in rows:

        print(row["userid"])

        print(row["name"]) 

        print(row["visits"])
   

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()
