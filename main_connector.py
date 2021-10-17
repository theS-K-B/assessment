# libraries needed
import mysql.connector
import pandas as pd
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(
        user     = 'root',
        password = '12345',
        host     = '127.0.0.1',
        database = 'test_db'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
